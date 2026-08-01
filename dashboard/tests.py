from unittest.mock import patch

from django.db import OperationalError
from django.test import TestCase
from django.urls import reverse


class DashboardViewTests(TestCase):
    def test_patient_dashboard_renders(self):
        response = self.client.get(reverse('patients'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Patients')

    @patch('patients.models.Patient.objects.all', side_effect=OperationalError('no such table'))
    def test_patient_dashboard_handles_missing_table(self, mocked_all):
        response = self.client.get(reverse('patients'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Patients')
