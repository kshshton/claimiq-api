from django.db import models


class ComplaintDecision(models.Model):
    """Complaint decision choices as a separate model"""
    code = models.CharField(max_length=50, unique=True)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = "Complaint Decision"
        verbose_name_plural = "Complaint Decisions"
