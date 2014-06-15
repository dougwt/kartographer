from django.shortcuts import render, redirect

from .models import RacerStats, Racer, Body, Tire, Glider, KartConfig

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

    # Insert any potential new configuration
    test_data = (10, 19, 2, 2)
    if KartConfig(test_data).valid:
        config_list = request.session.get('config_list', [])
        config_list.append((10, 19, 2, 2))
        request.session['config_list'] = config_list

    # Convert config_list tuples into KartConfig objects
    configurations = []
    for config_data in request.session['config_list']:
        config = KartConfig(config_data)
        if config.valid:
            configurations.append(config)

    context = {
        'racerstats': RacerStats.objects.all(),
        'racers': Racer.objects.select_related().all(),
        'bodies': Body.objects.all(),
        'tires': Tire.objects.all(),
        'gliders': Glider.objects.all(),
        'configurations': configurations,
    }
    return render(request, 'home.html', context)

def items(request):
    context = {
        'racerstats': RacerStats.objects.all(),
        'racers': Racer.objects.select_related().all(),
        'bodies': Body.objects.all(),
        'tires': Tire.objects.all(),
        'gliders': Glider.objects.all(),

    }
    return render(request, 'items.html', context)

def reset(request):
    request.session['config_list'] = []
    return redirect('home')
