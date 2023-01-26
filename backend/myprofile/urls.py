from django.urls import include, path
from .views import *

urlpatterns = [
    path('api/drf-auth/', include('rest_framework.urls')),
    path('api/drf-admins/', My_Profile_Admins.as_view()),
    path('api/drf-admins/update/<int:pk>', My_Profile_Admins_Update.as_view()),
    path("", weather_def_to_create_a_weather_on_main_page, name='Home'),
    path('Docs/', Documentation_site_page.as_view(), name='Docs'),
    path('information/', information_site_page.as_view(), name='information'),
]
