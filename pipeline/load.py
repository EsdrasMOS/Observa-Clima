import os
import django
# Permite usa o Django ORM fora do servidor (em script python)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'observaclima.settings')
django.setup()
from climate.models import WeatherRecord

class LoadError(Exception):
    pass

# Carrega os dados do DF para o BD do postgres
def load_to_database(df, city_name: str = "Recife") -> int:
    try:
        records_saved = 0
        # Vai iterar por cada linha do DF
        for _, row in df.iterrows():
            # Verifica se já tem um registro para esta data e cidade
            existing = WeatherRecord.objects.filter(
                date=row['date'],
                city=city_name
            ).exists()
            # Se existir, atualiza o registro
            if existing:
                WeatherRecord.objects.filter(
                    date=row['date'],
                    city=city_name
                ).update(
                    temp_max=row['temp_max'],
                    temp_min=row['temp_min'],
                    temp_avg=row['temp_avg'],
                    precipitation=row['precipitation']
                )
            # Se não existe, cria um novo registro
            else:
                WeatherRecord.objects.create(
                    date=row['date'],
                    temp_max=row['temp_max'],
                    temp_min=row['temp_min'],
                    temp_avg=row['temp_avg'],
                    precipitation=row['precipitation'],
                    city=city_name
                )
            
            records_saved += 1
        
        return records_saved
    
    except Exception as e:
        raise LoadError(f"Erro ao carregar dados no banco: {e}")