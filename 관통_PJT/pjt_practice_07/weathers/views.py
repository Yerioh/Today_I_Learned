from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse

import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import WeatherSerializer
from .models import Weather

# Create your views here.
@api_view(['GET'])
def index(request):
    api_key = settings.API_KEY
    city_name = 'Seoul,KR'
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}'
    response = requests.get(url).json()
    return Response(response)


def save_data(request):
    api_key = settings.API_KEY
    city_name = 'Seoul,KR'
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}'
    response = requests.get(url).json()
    for li in response.get('list'):
        dt_txt = li.get('dt_txt')
        temp = li.get('main').get('temp')
        feels_like = li.get('main').get('feels_like')

        if Weather.objects.filter(dt_txt=dt_txt, temp=temp, feels_like=feels_like).exists():
            continue
        
        data = {
            'dt_txt': dt_txt,
            'temp': temp,
            'feels_like': feels_like
        }


        serializer = WeatherSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    
    return JsonResponse({'message': '저장 성공'})
    