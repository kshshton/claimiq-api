from django.db import models


class ComplaintType(models.TextChoices):
    """Complaint type choices"""
    GUARANTEE = 'guarantee', 'Gwarancja'
    WARRANTY = 'warranty', 'Rękojmia'
