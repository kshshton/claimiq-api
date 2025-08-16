import datetime
import uuid

from django.core.validators import MinValueValidator
from django.db import models


class Complaint(models.Model):
    """Complaint model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.CharField(max_length=50, unique=True)
    commodity_name = models.CharField(max_length=255)
    type = models.ForeignKey(
        "ComplaintType",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="complaints",
        default=None
    )
    submit_date = models.DateField(auto_now_add=True)
    date_of_purchase = models.DateField(default=datetime.date.today)
    exit_date = models.DateField(null=True, blank=True)

    # New fields
    barcode = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField(
        blank=True, null=True, validators=[MinValueValidator(0)])
    producer = models.ForeignKey(
        "Producer",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="complaints"
    )
    registration_unit = models.ForeignKey(
        "RegistrationUnit",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="complaints"
    )
    description = models.TextField(blank=True, null=True)
    demand = models.TextField(blank=True, null=True)
    status = models.ForeignKey(
        "ComplaintStatus",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="complaints"
    )
    decision = models.ForeignKey(
        "ComplaintDecision",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="complaints",
        default=None
    )

    # Relation
    user = models.ForeignKey(
        'User', on_delete=models.SET_NULL, null=True, blank=True, related_name='complaints')

    def __str__(self):
        return f"Complaint {self.number}"
