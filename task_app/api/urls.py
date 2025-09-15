from django.urls import path

from task_app.api import views

urlpatterns = [
    path('list/', views.TaskListView.as_view(), name="task-list"),
    path('task-create/', views.TaskCreateView.as_view(), name="task-create"),
    path('<int:pk>', views.TaskDetailView.as_view(), name="task-details"),
    path('task-assign/', views.TaskAssignUserView.as_view(), name="task-assign"),
    path("<int:task_id>/comments/",
         views.CommentListView.as_view(), name="comments"),
    path("comments/<int:pk>", views.CommentDetailView.as_view(),
         name="comment-details"),
]
