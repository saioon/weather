from django.urls import path
from . import views
from .views import previsao_tempo


urlpatterns = [
    path('', views.weather, name='weather'),
    path('previsao_tempo/', previsao_tempo, name='previsao_tempo'),
]
