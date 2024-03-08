from django.shortcuts import render
from .models import aisDataTable
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import aisDataTableSerializer
from emissions_django_backend.utils.journeyDistance import calculate_journey_distance
from emissions_django_backend.utils.fuelConsumption import calculate_speed_time_fuel
from django.db.models import Q
from datetime import datetime

@api_view(['GET'])
def api_test_table_view(request):
    # get vessel_name parameter from the request's query parameters
    vessel_name = request.query_params.get('vessel_name')
    #get start date
    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')
    #gilter queryset based on vessel_name (if provided)
    #convert string to datetime
    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d").date()
    #convert date time to the minimum and maximum times as we are only inputting days, not times
    start_datetime = datetime.combine(start_date_obj, datetime.min.time())
    end_datetime = datetime.combine(end_date_obj, datetime.max.time())
    queryset = aisDataTable.objects.all()
    if vessel_name:
        #Q here allows for case insensitive search
        queryset = queryset.filter(
                    Q(vessel_name__iexact=vessel_name)&
                    Q(message_timestamp__date__gte=start_datetime.date()) &
                    Q(message_timestamp__date__lte=end_datetime.date())
        )
    #order queryset by message_timestamp
    queryset = queryset.order_by('message_timestamp')

    #serialise the queryset
    serializer = aisDataTableSerializer(queryset, many=True)

    #return the serialized data in the response
    return Response(serializer.data)

@api_view(['GET'])
def api_get_distance(request):
    #get vessel_name parameter from the request's query parameters
    vessel_name = request.query_params.get('vessel_name')
    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')
    #gilter queryset based on vessel_name (if provided)
    #convert string to datetime
    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d").date()
    #convert date time to the minimum and maximum times as we are only inputting days, not times
    start_datetime = datetime.combine(start_date_obj, datetime.min.time())
    end_datetime = datetime.combine(end_date_obj, datetime.max.time())
    #filter queryset based on vessel_name (if provided)
    queryset = aisDataTable.objects.all()
    if vessel_name:
                queryset = queryset.filter(
                    Q(vessel_name__iexact=vessel_name)&
                    Q(message_timestamp__date__gte=start_datetime.date()) &
                    Q(message_timestamp__date__lte=end_datetime.date())
        )

    #order queryset by message_timestamp
    queryset = queryset.order_by('message_timestamp')

    #serialise the queryset
    serializer = aisDataTableSerializer(queryset, many=True)
    #specifying nm here means it will trigger the if clause in the function and return distance in nm, not km
    distance = calculate_journey_distance(serializer.data, unit='nm')
    print("distance is ",distance)
    #return serialized data in the response
    return Response(distance)

@api_view(['GET'])
def api_get_fuel_consumption(request):
    #get the vessel_name parameter from the request's query parameters
    vessel_name = request.query_params.get('vessel_name')
    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')
    #gilter queryset based on vessel_name (if provided)
    #convert string to datetime
    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d").date()
    #convert date time to the minimum and maximum times as we are only inputting days, not times
    start_datetime = datetime.combine(start_date_obj, datetime.min.time())
    end_datetime = datetime.combine(end_date_obj, datetime.max.time())
    #filter queryset based on vessel_name (if provided)
    queryset = aisDataTable.objects.all()
    if vessel_name:
                queryset = queryset.filter(
                    Q(vessel_name__iexact=vessel_name)&
                    Q(message_timestamp__date__gte=start_datetime.date()) &
                    Q(message_timestamp__date__lte=end_datetime.date())
        )
    #order the queryset by message_timestamp
    queryset = queryset.order_by('message_timestamp')

    #serialize queryset
    serializer = aisDataTableSerializer(queryset, many=True)
    speeds = calculate_speed_time_fuel(serializer.data)
    print("speeds are ",speeds)
    # return serialised data inresponse
    return Response(speeds)
