import uuid

from django.db import models


def deleted_user_placeholder():
    return "Deleted user"


class ActionHistory(models.Model):
    """Action History model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.ForeignKey(
        'User',
        on_delete=models.SET(deleted_user_placeholder),
        to_field='email',
        db_column='email',
    )
    action = models.ForeignKey(
        "ActionType",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="action_history",
        default=None
    )
    date = models.DateField(auto_now_add=True)
    details = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Action History"

    def __str__(self):
        return f"{self.action} by {self.email} on {self.date}"
