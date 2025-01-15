from django.conf import settings
from django.db import models

# Create your models here.
class Report(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='assigned_reports'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.address}"