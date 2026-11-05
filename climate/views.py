from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg, Max, Min, Sum
from datetime import timedelta
from django.utils import timezone
from .models import WeatherRecord
from .serializers import WeatherRecordSerializer
from django.db.models import Avg, Max, Min, Sum, Count
from django.db.models.functions import TruncMonth
from datetime import timedelta
from django.utils import timezone

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
    # O dia mais quente, mais frio ou mais chuvoso
    @action(detail=False, methods=['get'])   
    def extremes(self, request):
        queryset = self.get_queryset()
        # Mis quente
        hottest = queryset.order_by('-temp_max').first()
        # Mais frio
        coldest = queryset.order_by('temp_min').first()
        # Mais chuvoso
        rainiest = queryset.order_by('-precipitation').first()
        serializer = self.get_serializer([hottest, coldest, rainiest], many=True)
        # Organizando a semântica da resposta
        data = {
            "hottest_day": serializer.data[0] if hottest else None,
            "coldest_day": serializer.data[1] if coldest else None,
            "rainiest_day": serializer.data[2] if rainiest else None
        }
        return Response(data)
    # Endpoint com total de chuva de cada mês que há no banco
    @action(detail=False, methods=['get'])
    def monthly(self, request):
        queryset = self.get_queryset().annotate(
            month=TruncMonth('date')
        ).values('month').annotate(
            total_precipitation=Sum('precipitation'),
            avg_temp=Avg('temp_avg'),
            record_count=Count('id')
        ).order_by('month')
        
        # Formatar as datas para o JSON
        formatted_data = []
        for item in queryset:
            formatted_data.append({
                "month": item['month'].strftime('%Y-%m'),
                "total_precipitation_mm": round(item['total_precipitation'] or 0, 1),
                "avg_temp_celsius": round(item['avg_temp'] or 0, 1),
                "days_recorded": item['record_count']
            })
        return Response(formatted_data)
    # Endpoint com os dados diários dos últimos 30 dias + média móvel de 7 dias
    @action(detail=False, methods=['get'])
    def trends(self, request):
        latest_date = timezone.now().date()
        start_date = latest_date - timedelta(days=30)
        
        # Busca os dados ordenados por data para calcular a média móvel
        queryset = self.get_queryset().filter(
            date__gte=start_date,
            date__lte=latest_date
        ).order_by('date')
        
        data = []
        temps = []
        
        for record in queryset:
            temps.append(record.temp_avg)
            # Calcula a média móvel de 7 dias
            if len(temps) >= 7:
                moving_avg = sum(temps[-7:]) / 7
            else:
                # Média dos dias disponíveis no início
                moving_avg = sum(temps) / len(temps) 
                
            data.append({
                "date": record.date.strftime('%Y-%m-%d'),
                "temp_avg": round(record.temp_avg, 1),
                "moving_avg_7d": round(moving_avg, 1),
                "precipitation": round(record.precipitation, 1)
            })
            
        return Response(data)

# Import para o action stats
from django.db.models import Count