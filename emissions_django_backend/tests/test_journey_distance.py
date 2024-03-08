from datetime import datetime
from django.test import TestCase
from emissions_django_backend.utils.journeyDistance import calculate_journey_distance

class CalculateJourneyDistanceTestCase(TestCase):
    def test_calculate_journey_distance(self):
        data_list = [
            {'latitude': 34.56789, 'longitude': -123.45678, 'message_timestamp': '2023-04-01T12:34:56'},
            {'latitude': 34.67890, 'longitude': -123.56789, 'message_timestamp': '2023-04-01T13:34:56'},
        ]

        #clac journey distance
        result = calculate_journey_distance(data_list)

        #expected behaviour
        print("result ",result)
        self.assertGreaterEqual(result, 0)

