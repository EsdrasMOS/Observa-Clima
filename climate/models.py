from django.db import models

# Tabela de registro meteorológico diário
class WeatherRecord(models.Model):
    # Data do registro
    date = models.DateField(
        verbose_name="Data",
        help_text="Data do registro meteorológico"
    )
    
    # Temperatura máxima do dia
    temp_max = models.FloatField(
        verbose_name="Temperatura Máxima (°C)",
        help_text="Temperatura máxima registrada no dia"
    )
    
    # Temperatura mínima
    temp_min = models.FloatField(
        verbose_name="Temperatura Mínima (°C)",
        help_text="Temperatura mínima registrada no dia"
    )
    
    # Temperatura média
    temp_avg = models.FloatField(
        verbose_name="Temperatura Média (°C)",
        help_text="Temperatura média do dia (calculada)"
    )
    
    # Precipitação total
    precipitation = models.FloatField(
        verbose_name="Precipitação (mm)",
        help_text="Total de precipitação no dia"
    )
    
    # Nome da cidade
    city = models.CharField(
        max_length=100,
        verbose_name="Cidade",
        help_text="Nome da cidade do registro",
        default="Recife"
    )
    
    # Momento que o registro foi criado no banco
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Criado em",
        help_text="Data e hora de criação do registro"
    )
    
# Dados do modelo 
    class Meta:
        verbose_name = "Registro Meteorológico"
        verbose_name_plural = "Registros Meteorológicos"
        # Ordena por data decrescente (mais recente primeiro)
        ordering = ['-date']  
        # Não pode haver dois registros para a mesma data e cidade
        unique_together = [['date', 'city']]  
    
    def __str__(self):
        return f"{self.city} - {self.date}: Max {self.temp_max}°C, Min {self.temp_min}°C"
    

# PARA VERIFICAR OS DADOS NO BANCO, PODE SER FEITO NO "python manage.py shell" e adicionando:
"""
from climate.models import WeatherRecord

# Conta quantos registros existem
WeatherRecord.objects.count()
# Deve retornar: 91

# Mostra os 5 registros mais recentes
for record in WeatherRecord.objects.all()[:5]:
    print(record)

# Sai do shell
exit()
"""

# NO PGADMIN PODE SER ACESSADO NA PRÓPRIA TABELA "climate_weaterrecord" > "view/edit data" > "all rows"
