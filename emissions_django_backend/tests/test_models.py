from django.test import TestCase
from emissions_django_backend.models import aisDataTable

#sanity check for testing
class SimpleMathTestCase(TestCase):
    def test_addition(self):
        result = 2 + 2
        self.assertEqual(result, 4)

class AisDataTableModelTestCase(TestCase):
    def setUp(self):
        self.sample_data = {
            'vessel_name': 'Test Vessel',
            'vessel_imo': 1234567,
            'latitude': 34.56789,
            'longitude': -123.45678,
            'message_timestamp': '2023-04-01T12:34:56',
        }

    def test_model_str_representation(self):
        #create instance with  test data from above
        instance = aisDataTable(**self.sample_data)
        expected_str = f"{self.sample_data['vessel_name']} ({self.sample_data['vessel_imo']})"
        self.assertEqual(str(instance), expected_str)

    def test_model_meta_options(self):
        #checks the meta options of the class
        self.assertFalse(aisDataTable._meta.managed)  
        self.assertEqual(aisDataTable._meta.db_table, 'april_2023_data')  
        self.assertEqual(aisDataTable._meta.app_label, 'emissions_django_backend')  
