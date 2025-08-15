import datetime
import uuid

from django.core.validators import MinValueValidator
from django.db import models

from ..enums import ComplaintType, RegistrationUnit


class Complaint(models.Model):
    """Complaint model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.CharField(max_length=50, unique=True)
    type = models.CharField(
        max_length=20,
        choices=ComplaintType.choices
    )
    submit_date = models.DateField(auto_now_add=True)
    date_of_purchase = models.DateField(default=datetime.date.today)
    exit_date = models.DateField(null=True, blank=True)

    # New fields
    barcode = models.CharField(max_length=100, blank=True, null=True)
    quantity_of_good = models.IntegerField(
        blank=True, null=True, validators=[MinValueValidator(0)])
    registration_unit = models.CharField(
        max_length=20,
        choices=RegistrationUnit.choices,
        blank=True,
        null=True
    )
    description = models.TextField(blank=True, null=True)
    demand = models.TextField(blank=True, null=True)
    status = models.ForeignKey(
        "ComplaintStatus",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="complaints"
    )
    decision = models.ForeignKey(
        "ComplaintDecision",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="complaints"
    )

    # Relation
    user = models.ForeignKey(
        'User', on_delete=models.SET_NULL, null=True, blank=True, related_name='complaints')

    def __str__(self):
        return f"Complaint {self.number}"


class ComplaintDecision(models.Model):
    """Complaint decision choices as a separate model"""
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = "Complaint Decision"
        verbose_name_plural = "Complaint Decisions"


class ComplaintStatus(models.Model):
    """Complaint status choices as a separate model"""
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = "Complaint Status"
        verbose_name_plural = "Complaint Statuses"
