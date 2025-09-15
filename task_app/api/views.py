from django.db.models import Q

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from task_app.api import serializers
from task_app.models import Task, Comment
from common.permissions import IsAdmin, IsAdminOrManager, IsTaskOwnerOrReadOnly, IsCommentOwnerOrReadOnly
from common.decorators import timer


class TaskListView(APIView):

    permission_classes = [IsAdminOrManager]

    # @timer
    def get(self, request):
        search_query = request.query_params.get('search', None)
        tasks = Task.objects.all().order_by('created_at')

        if search_query:
            tasks = tasks.filter(
                Q(title__icontains=search_query) |
                Q(status__icontains=search_query) |
                Q(priority__icontains=search_query) |
                Q(users__username=search_query)
            )

        serializer = serializers.TaskSerializer(tasks, many=True)
        data = {
            "success": True,
            "task": serializer.data
        }

        return Response(data, status=status.HTTP_200_OK)


class TaskCreateView(APIView):

    permission_classes = [IsAdmin]

    def post(self, request):
        serializer = serializers.TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "success": True,
                "message": "Task Created successfully",
                "task": serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {
                "success": False,
                "message": "task not created",
            }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = [IsTaskOwnerOrReadOnly]


class TaskAssignUserView(APIView):
    permission_classes = [IsAdminOrManager]

    def post(self, request):
        serializer = serializers.TaskAssignUserView(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "success": True,
                "message": f"Task assigned to the user successfully."
                # "message": f"Task {serializer.data["task"]} assigned to the user {serializer.data["user"]} successfully."
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {
                "success": False,
                "message": "Something went wrong."
            }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


class CommentListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, task_id):
        comments = Comment.objects.filter(task=task_id).order_by('-created')
        serializer = serializers.CommentSerializer(comments, many=True)
        data = {
            "success": True,
            "message": "Comments fetched successfully",
            "data": serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response(
                {"success": False, "message": "Task not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = serializers.CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user, task=task)
            return Response(
                {
                    "success": True,
                    "message": "Comment posted successfully",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            {
                "success": False,
                "message": "Validation failed",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsCommentOwnerOrReadOnly]
