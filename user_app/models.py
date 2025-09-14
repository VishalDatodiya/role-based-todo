from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Roles
    ADMIN = 'ADMIN'
    MANAGER = 'MANAGER'
    EMPLOYEE = 'EMPLOYEE'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (EMPLOYEE, 'Employee'),
    ]

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=EMPLOYEE)

    # username will still exist from AbstractUser, but we can make email primary for login later if needed
    def __str__(self):
        return f"{self.username} ({self.role})"
