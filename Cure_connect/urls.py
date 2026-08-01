from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('patients/', views.patient_dashboard, name='patients'),
    path('doctors/', views.doctor_dashboard, name='doctors'),
    path('appointments/', views.appointment_dashboard, name='appointments'),
]