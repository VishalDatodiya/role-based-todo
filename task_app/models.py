from django.db import models
from django.conf import settings

from user_app.models import User


class Task(models.Model):
    STATUS_CHOICES = (
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
    )

    PRIORITY_CHOICES = (
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    )

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="todo")
    priority = models.CharField(
        max_length=20, choices=PRIORITY_CHOICES, default="medium")

    due_date = models.DateTimeField(null=True, blank=True)

    # 👇 connect Task ↔ User via UserTask mapping
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through="UserTask",
        related_name="assigned_tasks"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class UserTask(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    assign_date = models.DateTimeField(auto_now_add=True)
    last_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'task')  # prevent duplicate assignments

    def __str__(self):
        return f"{self.user.username} -> {self.task.title}"


class Comment(models.Model):
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + " | " + self.text[:20]
