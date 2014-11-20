"""Django views for displaying and comparing MK8 kart configurations."""

import json
import locale
import logging
import random

import settings.base as settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.db.models import F
from django.shortcuts import (get_list_or_404, get_object_or_404, redirect,
                              render)
from ipware.ip import get_ip, get_real_ip

from .models import (Character, CharacterStats, ConfigList, ConfigListItem,
                     Glider, Kart, KartConfig, Wheel)

logger = logging.getLogger(__name__)


def log(msg, request):
    """Log a message with the attached request IP address."""
    ip = get_real_ip(request)
    if ip is None:
        ip = get_ip(request)
    logger.info("[%s] %s" % (ip, msg))


def fetch_random_quote():
    file_path = "%s/comparison/quotes.txt" % settings.SITE_ROOT
    with open(file_path, 'r') as f:
        read_data = f.read()

    if read_data:
        quotes = read_data.splitlines()
        return random.choice(quotes)


def home(request):
    """Display the visitor's config list and form to add a new config."""
    # Convert config_list tuples (session variable) into KartConfig objects
    configurations = []
    for config_data in request.session.get('config_list', []):
        config = KartConfig(config_data)
        if config.valid:
            configurations.append(config)

    log('Displaying My List page', request)

    total_combinations = Character.objects.count() * \
                       Kart.objects.count() * \
                       Wheel.objects.count() * \
                       Glider.objects.count()

    column_prefs = {
        'speed': request.session.get('show_col_speed', None),
        'speed_hidden': request.session.get('show_col_speed_hidden', None),
        'acceleration': request.session.get('show_col_acceleration', None),
        'weight': request.session.get('show_col_weight', None),
        'handling': request.session.get('show_col_handling', None),
        'handling_hidden': request.session.get('show_col_handling_hidden', None),
        'traction': request.session.get('show_col_traction', None),
        'miniturbo': request.session.get('show_col_miniturbo', None),
        'highlight_hidden': request.session.get('show_col_highlight_hidden', None),
        'highlight_acceleration': request.session.get('show_col_highlight_acceleration', None),
    }

    context = {
        'characterstats':       CharacterStats.objects.all(),
        'characters':           Character.objects.select_related().all(),
        'karts':                Kart.objects.all(),
        'wheels':               Wheel.objects.all(),
        'gliders':              Glider.objects.all(),
        'configurations':       configurations,
        'column_prefs':         json.dumps(column_prefs),
        'total_combinations':   total_combinations,
        'total_list_count':     len(ConfigList.objects.all()),
        'total_config_count':   len(ConfigListItem.objects.all()),
        'quote':                fetch_random_quote(),
    }
    return render(request, 'comparison/home.html', context)


def add(request):
    """Display the visitor's config list and form to add a new config."""
    # Insert any potential new configurations that were submitted
    if request.method == "POST":
        potential_config = (
            request.POST.get('add-character', ''),
            request.POST.get('add-kart', 'test string'),
            request.POST.get('add-wheel', ''),
            request.POST.get('add-glider', '')
        )

        potential_config = [unicode(item) for item in potential_config]
        if '' in potential_config:
            msg = 'Unable to add kart. Please choose a component for each ' \
                  'section and try again.'
            messages.add_message(request, messages.ERROR, msg)

        elif potential_config in request.session.get('config_list', []):
            msg = 'The configuration you added already exists in your list.'
            messages.add_message(request, messages.WARNING, msg)

            log('Rejecting duplicate configuration %s' % potential_config,
                request)

        elif KartConfig(potential_config).valid:
            config_list = request.session.get('config_list', [])
            config_list.append(potential_config)
            request.session['config_list'] = config_list

            msg = 'Your kart configuration was added successfully.'
            messages.add_message(request, messages.SUCCESS, msg)

            log('Adding configuration %s' % potential_config, request)

            # Redirect to My List
            return redirect('home')

    log('Displaying Add page', request)

    context = {
        'characterstats':       CharacterStats.objects.all(),
        'characters':           Character.objects.select_related().all(),
        'karts':                Kart.objects.all(),
        'wheels':               Wheel.objects.all(),
        'gliders':              Glider.objects.all(),
        'total_list_count':     len(ConfigList.objects.all()),
        'total_config_count':   len(ConfigListItem.objects.all()),
        'quote':                fetch_random_quote(),
    }
    return render(request, 'comparison/add.html', context)


def components(request):
    """List all kart components and their stats."""
    log('Displaying Kart Components page', request)

    components = [
        {
            'name': 'character',
            'plural': 'characters',
            'items': Character.objects.select_related().all(),
        },
        {
            'name': 'kart',
            'plural': 'karts',
            'items': Kart.objects.all(),
        },
        {
            'name': 'wheel',
            'plural': 'wheels',
            'items': Wheel.objects.all(),
        },
        {
            'name': 'glider',
            'plural': 'gliders',
            'items': Glider.objects.all(),
        },
    ]

    column_prefs = {
        'name': request.session.get('show_col_name', None),
        'speed': request.session.get('show_col_speed', None),
        'speed_hidden': request.session.get('show_col_speed_hidden', None),
        'acceleration': request.session.get('show_col_acceleration', None),
        'weight': request.session.get('show_col_weight', None),
        'handling': request.session.get('show_col_handling', None),
        'handling_hidden': request.session.get('show_col_handling_hidden', None),
        'traction': request.session.get('show_col_traction', None),
        'miniturbo': request.session.get('show_col_miniturbo', None),
        'highlight_hidden': request.session.get('show_col_highlight_hidden', None),
        'highlight_acceleration': request.session.get('show_col_highlight_acceleration', None),
    }

    context = {
        'characterstats':       CharacterStats.objects.all(),
        'components':           components,
        'column_prefs':         json.dumps(column_prefs),
        'total_list_count':     len(ConfigList.objects.all()),
        'total_config_count':   len(ConfigListItem.objects.all()),
        'quote':                fetch_random_quote(),
    }
    return render(request, 'comparison/components.html', context)


def reset(request):
    """Erase the visitor's config list."""
    request.session['config_list'] = []

    log('Resetting My List', request)

    return redirect('home')


def save(request):
    """Save the visitor's config list to a publicly viewable url."""
    # Convert config_list tuples (session variable) into KartConfig objects
    configurations = []
    for config_data in request.session.get('config_list', []):
        config = KartConfig(config_data)
        if config.valid:
            configurations.append(config)

    if configurations:

        # Create a ConfigList record for the new list
        config_list = ConfigList.create(request)
        config_list.save()

        # Create ConfigListItem records for each configuration in this list
        for config in configurations:
            item = ConfigListItem.create(config_list,
                                         config.character,
                                         config.kart,
                                         config.wheel,
                                         config.glider)
            try:
                item.save()
            except IntegrityError:
                pass

        # Create a success message
        location = reverse('list', args=[config_list.url])
        full_url = request.build_absolute_uri(location)
        msg = ('Your current list has been saved to <a href="%s" '
               'class="alert-link">%s</a>. Any additional changes you make '
               'will need to be re-shared.' % (full_url, full_url))
        messages.add_message(request, messages.SUCCESS, msg, extra_tags='safe')

        log('Saving list to %s' % full_url, request)

        # Redirect to the new url
        return redirect('list', url_hash=config_list.url)

    else:

        log('Rejected save attempt', request)

        # Redirect to My List
        return redirect('home')


def list(request, url_hash):
    """Display a saved KartConfigList based on given url hash."""
    config_list_obj = get_object_or_404(ConfigList, url=url_hash)
    config_list = get_list_or_404(ConfigListItem, list_id=config_list_obj.id)

    # If this session hasn't previously visisted this list, increase its view
    # counter and add its hash to the 'visited_lists' session variable.
    visited_lists = request.session.get('visited_lists', [])
    if url_hash not in visited_lists:
        visited_lists.append(url_hash)
        request.session['visited_lists'] = visited_lists
        ConfigList.objects.filter(url=url_hash).update(
            view_count=F('view_count')+1)

    # Convert config_list tuples into KartConfig objects
    configurations = []
    for config_data in config_list:
        config = KartConfig((config_data.character.id,
                             config_data.kart.id,
                             config_data.wheel.id,
                             config_data.glider.id))
        if config.valid:
            configurations.append(config)

    log('Displaying list %s' % url_hash, request)

    column_prefs = {
        'speed': request.session.get('show_col_speed', None),
        'speed_hidden': request.session.get('show_col_speed_hidden', None),
        'acceleration': request.session.get('show_col_acceleration', None),
        'weight': request.session.get('show_col_weight', None),
        'handling': request.session.get('show_col_handling', None),
        'handling_hidden': request.session.get('show_col_handling_hidden', None),
        'traction': request.session.get('show_col_traction', None),
        'miniturbo': request.session.get('show_col_miniturbo', None),
        'highlight_hidden': request.session.get('show_col_highlight_hidden', None),
        'highlight_acceleration': request.session.get('show_col_highlight_acceleration', None),
    }

    context = {
        'characterstats':       CharacterStats.objects.all(),
        'characters':           Character.objects.select_related().all(),
        'karts':                Kart.objects.all(),
        'wheels':               Wheel.objects.all(),
        'gliders':              Glider.objects.all(),
        'configurations':       configurations,
        'column_prefs':         json.dumps(column_prefs),
        'total_list_count':     len(ConfigList.objects.all()),
        'total_config_count':   len(ConfigListItem.objects.all()),
        'quote':                fetch_random_quote(),
    }
    return render(request, 'comparison/list.html', context)


def top(request):
    """Display popular lists and configurations created by users."""
    log('Displaying top page', request)

    popular_lists = ConfigList.objects.order_by('-view_count')[0:10]
    context = {
        'popular_lists': popular_lists,
        'quote':                fetch_random_quote(),
    }
    return render(request, 'comparison/top.html', context)
