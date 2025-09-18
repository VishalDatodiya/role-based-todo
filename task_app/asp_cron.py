from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from task_app.models import Task
from django.conf import settings


def send_deadline_reminders():
    tommorow = timezone.now() + timezone.timedelta(days=1)
    tasks = Task.objects.filter(due_date__date=tommorow)        # extracts just the date portion from the datetime field.

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
        print("Reminder mail send to the user")


def start_scheduler():
    scheduler = BackgroundScheduler()
    # runs every day at 9 AM
    # scheduler.add_job(send_deadline_reminders, 'cron', hour=9)
    # for testing purpose run evry minutes
    scheduler.add_job(send_deadline_reminders, 'interval', minutes=1)
    scheduler.start()
