from django.shortcuts import render
from doctors.models import Doctor
from patients.models import Patient
from appointments.models import Appointment

# Create your views here.

def home(request):
    return render(request, "home.html")

def patient_dashboard(request):
    patients = Patient.objects.all()
    return render(request, "patient_dashboard.html", {"patients": patients})

def doctor_dashboard(request):
    doctors = Doctor.objects.all()
    return render(request, "doctor_dashboard.html", {"doctors": doctors})

def appointment_dashboard(request):
    appointments = Appointment.objects.all()
    return render(request, "appointment_dashboard.html", {"appointments": appointments})