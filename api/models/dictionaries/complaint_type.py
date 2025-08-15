from django.db import models


class ComplaintType(models.Model):
    """Complaint status choices as a separate model"""
    code = models.CharField(
        max_length=50, unique=True, null=True)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = "Complaint Type"
        verbose_name_plural = "Complaint Types"
