"""Django views for displaying and comparing MK8 kart configurations."""

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.db.models import F
from django.shortcuts import (get_list_or_404, get_object_or_404, redirect,
                              render)

from .models import (Body, ConfigList, ConfigListItem, Glider, KartConfig,
                     Racer, RacerStats, Tire)


def home(request):
    """Display the visitor's config list and form to add a new config."""
    # Insert any potential new configurations that were submitted
    if request.method == "POST":
        potential_config = (
            request.POST['add-racer'],
            request.POST['add-body'],
            request.POST['add-tire'],
            request.POST['add-glider']
        )
        potential_config = [unicode(item) for item in potential_config]
        if potential_config in request.session.get('config_list', []):
            msg = 'The configuration you added already exists in your list.'
            messages.add_message(request, messages.WARNING, msg)
        elif KartConfig(potential_config).valid:
            config_list = request.session.get('config_list', [])
            config_list.append(potential_config)
            request.session['config_list'] = config_list

    # Convert config_list tuples (session variable) into KartConfig objects
    configurations = []
    for config_data in request.session.get('config_list', []):
        config = KartConfig(config_data)
        if config.valid:
            configurations.append(config)

    context = {
        'racerstats':           RacerStats.objects.all(),
        'racers':               Racer.objects.select_related().all(),
        'bodies':               Body.objects.all(),
        'tires':                Tire.objects.all(),
        'gliders':              Glider.objects.all(),
        'configurations':       configurations,
        'total_list_count':     len(ConfigList.objects.all()),
        'total_config_count':   len(ConfigListItem.objects.all()),
    }
    return render(request, 'home.html', context)


def items(request):
    """List all kart items and their stats."""
    context = {
        'racerstats':           RacerStats.objects.all(),
        'racers':               Racer.objects.select_related().all(),
        'bodies':               Body.objects.all(),
        'tires':                Tire.objects.all(),
        'gliders':              Glider.objects.all(),
        'total_list_count':     len(ConfigList.objects.all()),
        'total_config_count':   len(ConfigListItem.objects.all()),
    }
    return render(request, 'items.html', context)


def reset(request):
    """Erase the visitor's config list."""
    request.session['config_list'] = []
    return redirect('home')


def save(request):
    """Save the visitor's config list to a publicly viewable url."""
    # Convert config_list tuples (session variable) into KartConfig objects
    configurations = []
    for config_data in request.session.get('config_list', []):
        config = KartConfig(config_data)
        if config.valid:
            configurations.append(config)

    # Create a ConfigList record for the new list
    config_list = ConfigList.create(request)
    config_list.save()

    # Create ConfigListItem records for each configuration in this list
    for config in configurations:
        item = ConfigListItem.create(config_list,
                                     config.racer,
                                     config.body,
                                     config.tire,
                                     config.glider)
        try:
            item.save()
        except IntegrityError:
            pass

    # Create a success message
    location = reverse('list', args=[config_list.url])
    full_url = request.build_absolute_uri(location)
    msg = ('Your current list has been saved to <a href="%s" '
           'class="alert-link">%s</a>. Any additional changes you make will '
           'need to be re-shared.' % (full_url, full_url))
    messages.add_message(request, messages.SUCCESS, msg, extra_tags='safe')

    # Redirect to the new url
    return redirect('list', url_hash=config_list.url)


def list(request, url_hash):
    """Display a saved KartConfigList based on given url hash."""
    config_list_obj = get_object_or_404(ConfigList, url=url_hash)
    config_list = get_list_or_404(ConfigListItem, list_id=config_list_obj.id)

    # If this session hasn't previously visisted this list, increase its view
    # counter and add its hash to the 'visisted_lists' session variable.
    visited_lists = request.session.get('visited_lists', [])
    if url_hash not in visited_lists:
        visited_lists.append(url_hash)
        request.session['visited_lists'] = visited_lists
        ConfigList.objects.filter(url=url_hash).update(
            view_count=F('view_count')+1)

    # Convert config_list tuples into KartConfig objects
    configurations = []
    for config_data in config_list:
        config = KartConfig((config_data.racer.id,
                             config_data.body.id,
                             config_data.tire.id,
                             config_data.glider.id))
        if config.valid:
            configurations.append(config)

    context = {
        'racerstats':           RacerStats.objects.all(),
        'racers':               Racer.objects.select_related().all(),
        'bodies':               Body.objects.all(),
        'tires':                Tire.objects.all(),
        'gliders':              Glider.objects.all(),
        'configurations':       configurations,
        'total_list_count':     len(ConfigList.objects.all()),
        'total_config_count':   len(ConfigListItem.objects.all()),
    }
    return render(request, 'list.html', context)
