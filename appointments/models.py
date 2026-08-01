from django.db import models

# Create your models here.
from django.db import models
from patients.models import Patient
from doctors.models import Doctor

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    date = models.DateField()
    time = models.TimeField()

    STATUS = [
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Completed", "Completed"),
    ]

    status = models.CharField(max_length=20, choices=STATUS, default="Pending")

    def __str__(self):
        return f"{self.patient} - {self.doctor}"