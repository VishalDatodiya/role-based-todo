from rest_framework import serializers

from task_app.models import Task, UserTask, Comment
from user_app.models import User

# creating this serializer to show some info of user in task list


class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class TaskSerializer(serializers.ModelSerializer):
    users = UserSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ["id", "title", "description", "status", "priority",
                  "due_date", "users"]


class TaskAssignUserView(serializers.ModelSerializer):
    class Meta:
        model = UserTask
        fields = ["id", "user", "task", "assign_date", "last_date"]


# Comment Serializers start

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', "task", "user"]
        read_only_fields = ['user', 'task']
