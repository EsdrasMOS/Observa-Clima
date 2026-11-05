from rest_framework import serializers
from .models import WeatherRecord

# Transforma os objetos de weatherrecord em JSON
class WeatherRecordSerializer(serializers.ModelSerializer):    
    class Meta:
        model = WeatherRecord
        fields = ['id', 'date', 'temp_max', 'temp_min', 'temp_avg', 
                  'precipitation', 'city', 'created_at']
        # Inalteraveis pela API
        read_only_fields = ['id', 'created_at']  