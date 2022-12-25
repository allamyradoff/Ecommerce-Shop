from django.shortcuts import render
from .models import *


import requests
from bs4 import BeautifulSoup


def index(request):

    menu_firts = Section.objects.filter(cat="HYZMATDAŞLARA")
    menu_second = Section.objects.filter(cat="HYZMATLAR")

    main_page_info = MainPage.objects.all()[:1]
    media = MediaSections.objects.all().order_by('-id')

    decress = Decress.objects.all()[0:2]
    decress_2 = Decress.objects.all()[2:4]
    decress_3 = Decress.objects.all()[4:6]

    flight = Flight.objects.all()
    flight_up = flight.filter(flight_category='DEPARTURE')
    flight_down = flight.filter(flight_category='ARRIVAL')

    context = {
        'main_page_info': main_page_info,
        'media': media,
        'decress': decress,
        'decress_2': decress_2,
        'decress_3': decress_3,
        'flight_up': flight_up,
        'flight_down': flight_down,
        'menu_firts':menu_firts,
        'menu_second':menu_second,
    }

    return render(request, 'tm/main_page.html', context)


def airlines_services(request):
    banner_info = BannerForAirlinesServices.objects.all()[0:1]
    services = AirlinesServices.objects.all()

    context = {
        'banner_info': banner_info,
        'services': services
    }
    return render(request, 'tm/airlines_services.html', context)


def services_detail(request, id):
    services = AirlinesServices.objects.get(id=id)

    context = {
        'services': services,
    }

    return render(request, 'tm/services_detail.html', context)


def about_us(request):

    about_us = AboutUs.objects.all()[:1]
    about_us_image = AboutUsImage.objects.all()

    context = {
        'about_us': about_us,
        'about_us_image': about_us_image,
    }
    return render(request, 'tm/about_us.html', context)


def services(request):

    banner = AirlinesServicesBanner.objects.all()[:1]
    mini_services = AirlinesServicesRightBar.objects.all()[:2]
    mini_services_2 = AirlinesServicesRightBar.objects.all()[2:4]

    services = AirlinesServicesDown.objects.all()

    context = {
        'banner': banner,
        'mini_services': mini_services,
        'mini_services_2': mini_services_2,
        'services': services,

    }
    return render(request, 'tm/services.html', context)


def administration(request):

    adminstartion_banner = AdministrationPage.objects.all()[:1]
    mission = Mission.objects.all()
    table = AdministrationTable.objects.all()

    context = {
        'adminstartion_banner': adminstartion_banner,
        'mission': mission,
        'table': table,
    }
    return render(request, 'tm/administration.html', context)


def gallery(request):
    gallery = Gallery.objects.all()

    context = {
        'gallery': gallery
    }

    return render(request, 'tm/gallery.html', context)


def online_table(request):
    banner = OnlineTableBanner.objects.all()[:1]

    flight = Flight.objects.all()
    flight_up = flight.filter(flight_category='DEPARTURE')
    flight_down  = flight.filter(flight_category='ARRIVAL')
    
    context = {
        'flight_up': flight_up,
        'flight_down': flight_down,
        'banner':banner
    }
    return render(request, 'tm/online_table.html', context)
    

def online_taxes(request):

    online_taxes = OnlineTaxesBanner.objects.all()[:1]

    context = {
        'online_taxes':online_taxes
    }

    return render(request, 'tm/online_taxes.html', context)


def all_flight(request):
    

    banner = AllFlightBanner.objects.all()[:1]


    all_flight = AllFlight.objects.all()
    flight_up = all_flight.filter(flight_category='DEPARTURE')
    flight_down = all_flight.filter(flight_category='ARRIVAL')

    context = {
        'banner':banner,
        'flight_up':flight_up,
        'flight_down':flight_down,
    }

    return render(request, 'tm/plan_flights.html', context)


def cargo(request):

    cargo = Cargo.objects.all()[:1]
    pdf = CargoPDF.objects.all()
    icon = AboutUs.objects.all()[:1]

    context = {
        'cargo':cargo,
        'pdf':pdf,
        'icon':icon
    }

    return render(request, 'tm/cargo.html', context)



def directions(request):
    banner = Directions.objects.all()[:1]
    direction = DirectionsPlane.objects.all()
   
    context = {
        'banner':banner,
        'direction':direction,
    }
    return render(request, 'tm/direction.html', context)

def directions_detail(request, id):
    direction = DirectionsPlane.objects.get(id=id)


    context = {
        'direction':direction
    }
    return render(request, 'tm/direction_detail.html', context)


def airline_check(request):
    check_info = FlightCheck.objects.all()[:1]

    context = {
        'check_info':check_info
    }
    return render(request, 'tm/airline_check.html', context)


def airlines_info(request, id):

    info = Section.objects.get(id=id)
    pdf = PDF.objects.filter(section__id=id)

    context = {
        'info': info,
        'pdf':pdf,
    }
    return render(request, 'tm/airlines_info.html', context)














































# def index(request):
#     if request.method == "POST":
#         city = request.POST['city']
#         source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=d8d31293bee740761c933823c09ea').read()
#         list_of_data = json.loads(source)

#         data = {
#             'country_code': str(list_of_data['sys']['country']),
#             'coordinate':str(list_of_data['coord']['lon']) + ', ' + str(list_of_data['coord']['lat']),
#             'temp':str(list_of_data['main']['temp']) + ' C',
#             'pressure':str(list_of_data['main']['pressure']),
#             'humidity':str(list_of_data['main']['humidity']),
#             'main':str(list_of_data['weather'][0]['main']),
#             'description':str(list_of_data['weather'][0]['description']),
#             'icon':str(list_of_data['weather'][0]['icon'])
#         }
#         print(data)
#     else:
#         data = {}

#     return render(request, 'index.html', data)
