from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg, Max, Min, Sum
from datetime import timedelta
from django.utils import timezone
from .models import WeatherRecord
from .serializers import WeatherRecordSerializer

# Endpoints para listar registros, buscar por ID e mostrar informação dos últimos 7 dias 
class WeatherRecordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WeatherRecord.objects.all()
    serializer_class = WeatherRecordSerializer
    # Busca por data
    lookup_field = 'date'  
    def get_object(self):
        date_str = self.kwargs.get('date')
        return WeatherRecord.objects.get(date=date_str)
    
    # Endpoint para estatísticas do período: /api/weather/stats/
    # @action decorator pra endpoints customizados
    @action(detail=False, methods=['get'])
    def stats(self, request):
        queryset = self.get_queryset()
        
        stats = queryset.aggregate(
            avg_temp_max=Avg('temp_max'),
            avg_temp_min=Avg('temp_min'),
            avg_temp_avg=Avg('temp_avg'),
            max_temp=Max('temp_max'),
            min_temp=Min('temp_min'),
            total_precipitation=Sum('precipitation'),
            total_records=Count('id')
        )
        
        # Arredonda para 1 casa decimal
        stats = {
            'avg_temp_max': round(stats['avg_temp_max'] or 0, 1),
            'avg_temp_min': round(stats['avg_temp_min'] or 0, 1),
            'avg_temp_avg': round(stats['avg_temp_avg'] or 0, 1),
            'max_temp': round(stats['max_temp'] or 0, 1),
            'min_temp': round(stats['min_temp'] or 0, 1),
            'total_precipitation': round(stats['total_precipitation'] or 0, 1),
            'total_records': stats['total_records'] or 0
        }
        
        return Response(stats)
    # Endpoint para os últimos 7 dias
    @action(detail=False, methods=['get'])
    def latest(self, request):
        latest_date = timezone.now().date()
        start_date = latest_date - timedelta(days=7)
        
        queryset = self.get_queryset().filter(
            date__gte=start_date,
            date__lte=latest_date
        ).order_by('-date')
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Import para o action stats
from django.db.models import Count