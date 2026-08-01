from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ADMIN = "ADMIN"
    DOCTOR = "DOCTOR"
    PATIENT = "PATIENT"

    ROLE_CHOICES = [
        (ADMIN, "Administrator"),
        (DOCTOR, "Doctor"),
        (PATIENT, "Patient"),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=PATIENT
    )

    def __str__(self):
        return f"{self.username} ({self.role})"