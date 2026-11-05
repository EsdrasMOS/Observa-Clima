from django.contrib import admin
from django.urls import path, include
# Principais rotas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('climate.urls')),  # Inclui as rotas do app climate
]