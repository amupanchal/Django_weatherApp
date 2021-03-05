from django.shortcuts import render,redirect
import requests
from .models import City
from .form import CityForm
# Create your views here.


def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=8907728b1fd4e6f8d8ce067cf8abbf83'


    if request.method == 'POST':
            form = CityForm(request.POST)
            form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather/weather.html', context)

# def delete_city(request, city_name):
#     City.objects.get(name=city_name).delete()

#     return redirect('home')
