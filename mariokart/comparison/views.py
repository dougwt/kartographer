from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.db import IntegrityError

from .models import RacerStats, Racer, Body, Tire, Glider, KartConfig, ConfigList, ConfigListItem

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
    if request.method == "POST":
        potential_config = (
            request.POST['add-racer'],
            request.POST['add-body'],
            request.POST['add-tire'],
            request.POST['add-glider']
        )
        potential_config = [unicode(item) for item in potential_config]
        if potential_config in request.session['config_list']:
            messages.add_message(request, messages.WARNING, 'The configuration you added already exists in your list.')
        elif KartConfig(potential_config).valid:
            config_list = request.session.get('config_list', [])
            config_list.append(potential_config)
            request.session['config_list'] = config_list

    # Convert config_list tuples into KartConfig objects
    configurations = []
    for config_data in request.session.get('config_list', []):
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

def save(request):
    # Convert config_list tuples into KartConfig objects
    configurations = []
    for config_data in request.session.get('config_list', []):
        config = KartConfig(config_data)
        if config.valid:
            configurations.append(config)

    # Create a ConfigList record for the new list
    config_list = ConfigList.create()
    config_list.save()
    # Create ConfigListItem records for each configuration in this list
    for config in configurations:
        item = ConfigListItem.create(config_list, config.racer, config.body, config.tire, config.glider)
        try:
            item.save()
        except IntegrityError:
            pass

    location = reverse('list', args=[config_list.url])
    full_url = request.build_absolute_uri(location)
    messages.add_message(request, messages.SUCCESS, 'Your current list has been saved to <a href="%s" class="alert-link">%s</a>. Any additional changes you make will need to be re-shared.' % (full_url, full_url), extra_tags='safe')
    return redirect('list', url_hash=config_list.url)

def list(request, url_hash):
    config_list_obj = get_object_or_404(ConfigList, url=url_hash)
    config_list = get_list_or_404(ConfigListItem, list_id=config_list_obj.id)

    # Convert config_list tuples into KartConfig objects
    configurations = []
    for config_data in config_list:
        config = KartConfig((config_data.racer.id, config_data.body.id, config_data.tire.id, config_data.glider.id))
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
    return render(request, 'list.html', context)
