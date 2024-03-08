
from django.contrib import admin
from django.urls import path
from .views import api_test_table_view
from .views import api_get_distance
from .views import api_get_fuel_consumption


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/test-table/', api_test_table_view, name='api_test_table_view'),
    path('api/get_distance/', api_get_distance, name='api_get_distance'),
    path('api/get_fuel_consumption/', api_get_fuel_consumption, name='api_get_fuel_consumption')
]
