
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from task_app.models import Task
from django.conf import settings


def send_due_soon_reminders():
    tommorow = timezone.now() + timedelta(days=1)
    tasks = Task.objects.filter(due_date__date=tommorow)
    
    for task in tasks:
        for user in task.users.all():
            subject = f"Reminder : task  '{task.title}' is due"
            message = f"""
                        Hello {user.username},
                        This is reminder that the task '{task.title}
                        is due on {task.due_date.strftime('%Y-%m-%d %H:%M')},
                        Please make sure to complete it on time.
                        """
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=True
            )
        