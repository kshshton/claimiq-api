import uuid

from django.db import models


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
