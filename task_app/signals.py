# task_app/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

from task_app.models import UserTask

@receiver(post_save, sender=UserTask)
def send_task_assignment_email(sender, instance, created, **kwargs):
    """
    Send email when a new UserTask is created (task assigned to user)
    """
    print("=========================")
    if created:
        user = instance.user
        task = instance.task

        subject = f"New Task Assigned: {task.title}"
        message = f"""
        Hi {user.username},

        You have been assigned a new task: {task.title}.
        Description: {task.description}
        Due Date: {task.due_date.strftime('%Y-%m-%d %H:%M') if task.due_date else 'No deadline'}

        Please check your task dashboard for details.
        """

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=True
        )
