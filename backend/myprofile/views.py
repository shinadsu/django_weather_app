
from django.views.generic import ListView
from rest_framework import generics
from .utils import *
from .models import Myprofile
from .serializers import MyProfileSerializer
from django.shortcuts import render, redirect
from .models import City
import requests
from .forms import *


# Django
class Documentation_site_page(DataMixin, ListView):
    template_name = "myprofile/Documentation.html"
    model = Myprofile

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_datamixin = self.get_user_context(
            title='weather.com')
        context_to_view_on_site = dict(list(context.items(
        )) + list(context_datamixin.items()))
        return context_to_view_on_site


class information_site_page(DataMixin, ListView):
    template_name = "myprofile/information.html"
    model = Myprofile

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_datamixin = self.get_user_context(
            title='weather.com')
        context_to_view_on_site = dict(list(context.items(
        )) + list(context_datamixin.items()))
        return context_to_view_on_site


def weather_def_to_create_a_weather_on_main_page(request):
    url_adress_weather = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=0bb9dcd611790e49af9f17c62bfc2646'

    form_to_create_a_weather = Add_City_Form()

    cities_from_database = City.objects.all()
    all_cities_list = []
    form = Add_City_Form(request.POST)
    

    for city in cities_from_database:
        responce = requests.get(url_adress_weather.format(city.name)).json()
        if responce.get('main'):
            city_info = {
                'city': city.name,
                'temp': responce['main']['temp'],
                'icon': responce['weather'][0]['icon'],
                'error': False,
            }
        else:
            city_info = {
                'city': city.name,
                'error': True,
            }

        all_cities_list.append(city_info)

    context = {'all_info': all_cities_list, 'form': form_to_create_a_weather}
    return render(request, 'myprofile/index.html', context)



# Django Rest FrameWork
class My_Profile_Admins(generics.ListCreateAPIView):
    queryset = Myprofile.objects.all()
    serializer_class = MyProfileSerializer


class My_Profile_Admins_Update(generics.RetrieveUpdateDestroyAPIView):
    queryset = Myprofile.objects.all()
    serializer_class = MyProfileSerializer
