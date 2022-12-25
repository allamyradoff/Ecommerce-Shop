from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('airlines_services/', airlines_services, name='airlines_services'),
    path('services_detail/<int:id>/', services_detail, name='services_detail'),
    path('about_us/', about_us, name='about_us'),
    path('services/', services, name='services'),
    path('administration/', administration, name="administration"),
    path('gallery/', gallery, name="gallery"),
    path('online_table/', online_table, name="online_table"),
    path('online_taxes/', online_taxes, name="online_taxes"),
    path('all_flight/', all_flight, name="all_flight"),
    path('cargo/', cargo, name="cargo"),
    path('directions/', directions, name="directions"),
    path('directions_detail/<int:id>/', directions_detail, name="directions_detail"),
    path('airline_check/', airline_check, name="airline_check"),
    path('airlines_info/<int:id>/', airlines_info, name="airlines_info"),
]