from django.db import models


class ComplaintType(models.TextChoices):
    """Complaint type choices"""
    GUARANTEE = 'guarantee', 'Gwarancja'
    WARRANTY = 'warranty', 'Rękojmia'


class RegistrationUnit(models.TextChoices):
    """Registration unit choices"""
    METER_LINEAR = 'meter_linear', 'Metr bieżący'
    METER_SQUARE = 'meter_square', 'Metr kwadratowy'
    METER_CUBIC = 'meter_cubic', 'Metr sześcienny'
    PIECE = 'piece', 'Sztuka'


class ComplaintStatus(models.TextChoices):
    """Complaint status choices"""
    NOT_STARTED = 'not_started', 'Not Started'
    IN_PROGRESS = 'in_progress', 'In Progress'
    ON_HOLD = 'on_hold', 'On Hold'
    COMPLETE = 'complete', 'Complete'
