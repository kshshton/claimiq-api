import uuid

from django.db import models

from ..enums import ActionType


class ActionHistory(models.Model):
    """Action History model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        to_field='email',
        db_column='email'
    )

    action = models.CharField(
        max_length=20,
        choices=ActionType.choices
    )
    date = models.DateField(auto_now_add=True)
    details = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Action Histories"

    def __str__(self):
        return f"{self.action} by {self.email} on {self.date}"
