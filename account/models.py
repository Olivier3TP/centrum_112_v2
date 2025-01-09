from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('medic', 'Medyk'),
        ('dispatcher', 'Dyspozytor'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='dispatcher')

    def __str__(self):
        return f'Profil użytkownika: {self.first_name} , {self.last_name}'