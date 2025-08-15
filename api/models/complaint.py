import datetime
import uuid

from django.core.validators import MinValueValidator
from django.db import models

from ..enums import ComplaintStatus, ComplaintType, RegistrationUnit


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

    status = models.CharField(
        max_length=20,
        choices=ComplaintStatus.choices,
        default=ComplaintStatus.NOT_STARTED
    )

    def __str__(self):
        return f"Complaint {self.number}"
