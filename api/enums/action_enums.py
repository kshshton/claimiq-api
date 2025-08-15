from django.db import models


class ActionType(models.TextChoices):
    """Action type choices"""
    CREATED = 'created', 'Created'
    UPDATED = 'updated', 'Updated'
    APPROVED = 'approved', 'Approved'
    REJECTED = 'rejected', 'Rejected'
    COMMENTED = 'commented', 'Commented'
