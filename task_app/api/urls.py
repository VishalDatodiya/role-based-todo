from django.urls import path

from task_app.api import views

urlpatterns = [
    path('list/', views.TaskListView.as_view(), name="task-list"),
    path('<int:pk>', views.TaskDetailView.as_view(), name="task-details"),
    path('task-assign/', views.TaskAssignUserView.as_view(), name="task-assign"),
]
