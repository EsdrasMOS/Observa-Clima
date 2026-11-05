from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Cria um router e registra o viewset
router = DefaultRouter()
router.register(r'weather', views.WeatherRecordViewSet, basename='weather')

# As URLs são criadas automaticamente pelo router
urlpatterns = [
    path('', include(router.urls)),
]