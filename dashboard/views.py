from django.db import OperationalError, ProgrammingError
from django.shortcuts import render

from appointments.models import Appointment
from doctors.models import Doctor
from patients.models import Patient


def _safe_queryset(model):
    try:
        return model.objects.all()
    except (OperationalError, ProgrammingError):
        return model.objects.none()


def home(request):
    return render(request, "home.html")


def patient_dashboard(request):
    patients = _safe_queryset(Patient)
    return render(request, "patient_dashboard.html", {"patients": patients})


def doctor_dashboard(request):
    doctors = _safe_queryset(Doctor)
    return render(request, "doctor_dashboard.html", {"doctors": doctors})


def appointment_dashboard(request):
    appointments = _safe_queryset(Appointment)
    return render(request, "appointment_dashboard.html", {"appointments": appointments})