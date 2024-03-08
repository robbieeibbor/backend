from django.test import TestCase
from django.db import connections
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from emissions_django_backend.models import aisDataTable

class DatabaseConnectionTestCase(TestCase):
    def test_database_connection(self):
        connection = connections['default']

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")

            connection_established = True
        except Exception as e:
            connection_established = False

        self.assertTrue(connection_established)

