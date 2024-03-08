from django.db import models

class aisDataTable(models.Model):
    vessel_name = models.CharField(blank=True, db_column='name')
    vessel_imo = models.IntegerField(primary_key=True, db_column='imo')
    latitude = models.DecimalField(max_digits=15, decimal_places=8, null=True, blank=True, db_column="latitude")
    longitude = models.DecimalField(max_digits=15, decimal_places=8, null=True, blank=True, db_column="longitude")
    message_timestamp = models.DateTimeField(db_column='date_time_utc')

    class Meta:
        managed = False
        db_table = 'april_2023_data'
        app_label = 'emissions_django_backend' 

    def __str__(self):
        return f"{self.vessel_name} ({self.vessel_imo})"
