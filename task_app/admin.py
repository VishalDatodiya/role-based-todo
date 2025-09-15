from django.contrib import admin

from task_app.models import Task, UserTask, Comment

admin.site.register(Task)
admin.site.register(UserTask)
admin.site.register(Comment)
