from django.core.management import BaseCommand
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from task_app.models import Task


class Command(BaseCommand):

    help = "Send email for deadline reminder for task"

    def handle(self, *args, **options):
        tommorow = timezone.now() + timezone.timedelta(days=1)
        # extracts just the date portion from the datetime field.
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
                self.stdout.write(self.style.SUCCESS(f"Reminder sent to {user.email} for task {task.title}"))

        if not tasks.exists():
            self.stdout.write(self.style.WARNING("No tasks due tomorrow"))
