import unittest
from datetime import datetime
from emissions_django_backend.utils.fuelConsumption import calculate_speed_time_fuel

class TestCalculateSpeedTimeFuel(unittest.TestCase):

    def test_calculate_speed_time_fuel(self):
        sample_data = [
            {'latitude': 34.56789, 'longitude': -123.45678, 'message_timestamp': '2023-04-01T12:34:56'},
            {'latitude': 34.67890, 'longitude': -123.56789, 'message_timestamp': '2023-04-01T13:34:56'},
        ]

        result = calculate_speed_time_fuel(sample_data)

        self.assertIn('speeds', result)
        self.assertIn('times_in_days', result)
        self.assertIn('fuel_consumption', result)
        self.assertIn('fuel_consumed', result)
        self.assertIn('total_fuel_consumed', result)
        self.assertIn('co2_emissions', result)

        self.assertIsInstance(result['speeds'], list)
        self.assertIsInstance(result['times_in_days'], list)
        self.assertIsInstance(result['fuel_consumption'], list)
        self.assertIsInstance(result['fuel_consumed'], list)
        self.assertIsInstance(result['total_fuel_consumed'], float)
        self.assertIsInstance(result['co2_emissions'], float)

if __name__ == '__main__':
    unittest.main()
