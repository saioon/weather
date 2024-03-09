from django.shortcuts import render
import requests
from django.http import JsonResponse


def weather(request):
    city = 'caribe'  # Exemplo: Londres
    url = f'http://wttr.in/{city}?format=%C+%t'
    response = requests.get(url)
    weather_data = response.text
    return render(request, 'weather/weather.html', {'weather_data': weather_data})

def previsao_tempo(request):
    if request.method == 'POST':
        location = request.POST.get('location', '')
        # Aqui você faria a lógica real para obter os dados de previsão do tempo com base no local fornecido
        # Neste exemplo, estamos apenas retornando dados fixos
        weather_data = f"Previsão do tempo para {location}: 25°C, Ensolarado"
        return JsonResponse({'weather_data': weather_data})
    return render(request, 'previsao_tempo.html')

