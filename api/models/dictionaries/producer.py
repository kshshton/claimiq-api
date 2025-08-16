from django.db import models


class Producer(models.Model):
    """Producer model"""
    name = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.name
