from django.test import TestCase
from django.db import connections

class DatabaseConnectionTestCase(TestCase):
    def test_database_connection(self):
        # Getdefault db connection
        connection = connections['default']

        #chck connection is established
        try:
            with connection.cursor():
                pass
                print('\nconnection to db established\n')
            connection_is_established = True
        except Exception as e:
            connection_is_established = False

        #assert connection is established
        self.assertTrue(connection_is_established, "Failed to establish a connection postgres database.")
