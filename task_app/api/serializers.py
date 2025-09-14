from rest_framework import serializers

from task_app.models import Task, UserTask


class TaskSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ["id", "title", "description", "status", "priority",
                  "due_date", "users"]


class TaskAssignUserView(serializers.ModelSerializer):
    class Meta:
        model = UserTask
        fields = ["id", "user", "task", "assign_date", "last_date"]
