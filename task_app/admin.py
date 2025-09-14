from django.contrib import admin

from task_app.models import Task, UserTask

admin.site.register(Task)
admin.site.register(UserTask)
