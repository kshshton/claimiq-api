from django.db import models


class RegistrationUnit(models.Model):
    """Registration unit choices as a separate model"""
    code = models.CharField(
        max_length=50, unique=True, default="unit")
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = "Registration Unit"
        verbose_name_plural = "Registration Units"
