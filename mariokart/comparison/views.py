from django.shortcuts import render, redirect

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

    configurations = request.session.get('configurations', [])

    # Temporary data
    test_data = {
        'racer': {'file': "shyguy", 'name': "Shy Guy"},
        'body': {'file': "flamerider", 'name': "Flame Rider"},
        'tire': {'file': "monster", 'name': "Monster"},
        'glider': {'file': "cloudglider", 'name': "Cloud"},
        'speed': 2.75,
        'acceleration': 1.75,
        'weight': 3.25,
        'handling': 4.75,
        'traction': 2.50,
    }

    configurations.append(test_data)
    request.session['configurations'] = configurations

    context = {
        'racerstats': RacerStats.objects.all(),
        'racers': Racer.objects.select_related().all(),
        'bodies': Body.objects.all(),
        'tires': Tire.objects.all(),
        'gliders': Glider.objects.all(),
        'configurations': request.session['configurations'],
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
    request.session['configurations'] = []
    return redirect('home')
