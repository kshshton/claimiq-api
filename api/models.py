import uuid

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.db import models
from email_validator import EmailNotValidError, validate_email


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

    # Role choices
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        MANAGER = 'manager', 'Manager'
        USER = 'user', 'User'

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.USER
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


class Company(models.Model):
    """Company model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    logo = models.BinaryField(null=True, blank=True)
    company_name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10)
    town = models.CharField(max_length=100)
    nip = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=320, null=True, blank=True)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    branch_name = models.CharField(max_length=255, null=True, blank=True)
    branch_address = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.company_name


class Producer(models.Model):
    """Producer model"""
    name = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.name


class Complaint(models.Model):
    """Complaint model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.CharField(max_length=50, unique=True)

    # Complaint type choices
    class ComplaintType(models.TextChoices):
        LOGISTICS = 'logistics', 'Logistics'
        QUALITY = 'quality', 'Quality'
        CUSTOMER_SERVICE = 'customer_service', 'Customer Service'
        SAFETY = 'safety', 'Safety'

    type = models.CharField(
        max_length=20,
        choices=ComplaintType.choices
    )
    submit_date = models.DateField(auto_now_add=True)
    exit_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Complaint {self.number}"


class ActionHistory(models.Model):
    """Action History model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        to_field='email',
        db_column='email'
    )

    # Action choices
    class Action(models.TextChoices):
        CREATED = 'created', 'Created'
        UPDATED = 'updated', 'Updated'
        APPROVED = 'approved', 'Approved'
        REJECTED = 'rejected', 'Rejected'
        COMMENTED = 'commented', 'Commented'

    action = models.CharField(
        max_length=20,
        choices=Action.choices
    )
    date = models.DateField(auto_now_add=True)
    details = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Action Histories"

    def __str__(self):
        return f"{self.action} by {self.email} on {self.date}"
