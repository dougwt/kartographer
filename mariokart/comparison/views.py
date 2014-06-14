from django.shortcuts import render

from .models import RacerStats, Racer, Body, Tire, Glider

# Create your views here.
def add(request):
    context = {
        'racerstats': RacerStats.objects.all(),
        'racers': Racer.objects.select_related().all(),
        'bodies': Body.objects.all(),
        'tires': Tire.objects.all(),
        'gliders': Glider.objects.all(),

    }
    return render(request, 'add.html', context)

def home(request):
    # return HttpResponse("Hello, world. You're at the comparison home.")

    config = [
        {
            'racer': {'file': "75px-MK8_ShyGuy", 'name': "Shy Guy"},
            'body': {'file': "100px-FlameRiderBodyMK8", 'name': "Flame Rider"},
            'tire': {'file': "100px-MonsterTiresMK8", 'name': "Monster"},
            'glider': {'file': "100px-Cloud_Glider", 'name': "Cloud"},
            'speed': 2.75,
            'acceleration': 1.75,
            'weight': 3.25,
            'handling': 4.75,
            'traction': 2.50,
        }
    ]

    context = {
        'configurations': config * 6,
        'racerstats': RacerStats.objects.all(),
        'racers': Racer.objects.select_related().all(),
        'bodies': Body.objects.all(),
        'tires': Tire.objects.all(),
        'gliders': Glider.objects.all(),

    }
    return render(request, 'home.html', context)

def list(request):
    context = {
        'racerstats': RacerStats.objects.all(),
        'racers': Racer.objects.select_related().all(),
        'bodies': Body.objects.all(),
        'tires': Tire.objects.all(),
        'gliders': Glider.objects.all(),

    }
    return render(request, 'list.html', context)
