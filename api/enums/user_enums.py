from django.db import models


class UserRole(models.TextChoices):
    """User role choices"""
    ADMIN = 'admin', 'Admin'
    MANAGER = 'manager', 'Manager'
    USER = 'user', 'User'
