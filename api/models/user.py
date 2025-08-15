from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.db import models
from email_validator import EmailNotValidError, validate_email

from ..enums import UserRole


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Custom User model with email as primary key"""
    email = models.EmailField(primary_key=True, max_length=320, unique=True)
    first_name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    signature = models.BinaryField(null=True, blank=True)
    last_activity = models.DateTimeField(auto_now=True)

    role = models.CharField(
        max_length=10,
        choices=UserRole.choices,
        default=UserRole.USER
    )

    # Override username field to use email
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'surname']

    objects = CustomUserManager()

    def clean(self):
        super().clean()
        try:
            valid = validate_email(self.email)
            self.email = valid.email.lower()
        except EmailNotValidError as e:
            raise ValidationError(f"Invalid email address: {e}")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
