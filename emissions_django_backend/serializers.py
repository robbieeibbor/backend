
from rest_framework import serializers
from .models import aisDataTable

class aisDataTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = aisDataTable
        fields = '__all__'
