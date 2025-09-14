from django.urls import path

from user_app.api import view

urlpatterns = [
    path('login/', view.LoginView.as_view(), name="login"),
    path('register/', view.RegisterView.as_view(), name="register"),
]
