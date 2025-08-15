from django.db import models


class ActionType(models.Model):
    """Action type choices as a separate model"""
    code = models.CharField(
        max_length=50, unique=True, null=True)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = "Action Type"
        verbose_name_plural = "Action Types"
