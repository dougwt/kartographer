"""Django views for displaying and comparing MK8 kart configurations."""

import json
import logging
import random
import os
import datetime

from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.db.models import F
from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import (get_list_or_404, get_object_or_404, redirect,
                              render)
from ipware.ip import get_ip, get_real_ip

from .models import (Character, CharacterStats, ConfigList, ConfigListItem,
                     Glider, Kart, KartConfig, KartRecord, Wheel)

logger = logging.getLogger(__name__)


def log(msg, request):
    """Log a message with the attached request IP address."""
    ip = get_real_ip(request)
    if ip is None:
        ip = get_ip(request)
    logger.info("[%s] %s" % (ip, msg))


def fetch_update_datetime():
    git_cmd = 'git --git-dir="%s" log -1 --format=%%ci' % settings.GIT_ROOT
    update_timestamp = os.popen(git_cmd).read()
    format = "%Y-%m-%d %H:%M:%S -0800\n"

    return datetime.datetime.strptime(update_timestamp, format)


def fetch_random_quote():
    file_path = "%s/comparison/quotes.txt" % settings.SITE_ROOT
    with open(file_path, 'r') as f:
        read_data = f.read()

    if read_data:
        quotes = read_data.splitlines()
        return random.choice(quotes)


def random_hexcolor():
    r = lambda: random.randint(0, 255)
    return ('#%02X%02X%02X' % (r(), r(), r()))


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
        'speed_ground': request.session.get('show_col_speed_ground', None),
        'speed_hidden': request.session.get('show_col_speed_hidden', None),
        'acceleration': request.session.get('show_col_acceleration', None),
        'weight': request.session.get('show_col_weight', None),
        'handling_ground': request.session.get('show_col_handling_ground', None),
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
        'update_timestamp':     fetch_update_datetime(),
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

            record = {
                'character': Character.objects.get(pk=potential_config[0]),
                'kart': Kart.objects.get(pk=potential_config[1]),
                'wheel': Wheel.objects.get(pk=potential_config[2]),
                'glider': Glider.objects.get(pk=potential_config[3]),
            }

            KartRecord.objects.create(**record)

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
        'update_timestamp':     fetch_update_datetime(),
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
        'speed_ground': request.session.get('show_col_speed_ground', None),
        'speed_hidden': request.session.get('show_col_speed_hidden', None),
        'acceleration': request.session.get('show_col_acceleration', None),
        'weight': request.session.get('show_col_weight', None),
        'handling_ground': request.session.get('show_col_handling_ground', None),
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
        'update_timestamp':     fetch_update_datetime(),
        'quote':                fetch_random_quote(),
    }
    return render(request, 'comparison/components.html', context)

def components_redirect(request):
    """Redirect to the components page."""
    return redirect('components')

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
        'speed_ground': request.session.get('show_col_speed', None),
        'speed_hidden': request.session.get('show_col_speed_hidden', None),
        'acceleration': request.session.get('show_col_acceleration', None),
        'weight': request.session.get('show_col_weight', None),
        'handling_ground': request.session.get('show_col_handling', None),
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
        'config_list':          config_list_obj,
        'column_prefs':         json.dumps(column_prefs),
        'update_timestamp':     fetch_update_datetime(),
        'quote':                fetch_random_quote(),
    }
    return render(request, 'comparison/list.html', context)


def top(request):
    """Display popular lists and configurations created by users."""
    log('Displaying top page', request)

    popular_lists = ConfigList.objects.order_by('-view_count')[0:10]

    characters = Character.objects.select_related().all()
    character_stats = {character.name: {'count': len(KartRecord.objects.filter(character__name=character.name)), 'color': random_hexcolor()} for character in characters}
    character_stats = sorted(character_stats.items(), key=lambda (k, v): v['count'], reverse=True)

    karts = Kart.objects.select_related().all()
    kart_stats = {kart.name: {'count': len(KartRecord.objects.filter(kart__name=kart.name)), 'color': random_hexcolor()} for kart in karts}
    kart_stats = sorted(kart_stats.items(), key=lambda (k, v): v['count'], reverse=True)

    wheel = Wheel.objects.select_related().all()
    wheel_stats = {wheel.name: {'count': len(KartRecord.objects.filter(wheel__name=wheel.name)), 'color': random_hexcolor()} for wheel in wheel}
    wheel_stats = sorted(wheel_stats.items(), key=lambda (k, v): v['count'], reverse=True)

    gliders = Glider.objects.select_related().all()
    glider_stats = {glider.name: {'count': len(KartRecord.objects.filter(glider__name=glider.name)), 'color': random_hexcolor()} for glider in gliders}
    glider_stats = sorted(glider_stats.items(), key=lambda (k, v): v['count'], reverse=True)

    context = {
        'popular_lists':        popular_lists,
        'records':              KartRecord.objects.all(),
        'characters':           character_stats,
        'karts':                kart_stats,
        'wheels':               wheel_stats,
        'gliders':              glider_stats,
        'total_records':        KartRecord.objects.count(),
        'total_lists':          ConfigList.objects.count(),
        'update_timestamp':     fetch_update_datetime(),
        'quote':                fetch_random_quote(),
    }
    return render(request, 'comparison/top.html', context)


def ajax_set_preference(request):
    success = False
    to_return = {'msg': u'No POST data sent.'}
    if request.method == "POST":
        post = request.POST.copy()
        if post.has_key('preference') and post.has_key('value'):
            preference = post['preference']
            value = post['value']

            allowed_pref = ['name', 'speed_ground', 'speed_hidden', 'acceleration', 'weight', 'handling_ground', 'handling_hidden', 'traction', 'miniturbo', 'highlight_hidden', 'highlight_acceleration']
            allowed_value = ['true', 'false']

            if preference in allowed_pref and value in allowed_value:
                if value == 'true':
                    value = True
                else:
                    value = False
                request.session['show_col_' + preference] = value
                success = True
        else:
            to_return['msg'] = u"Requires both valid 'preference' and 'value'!"
    serialized = json.dumps(to_return)
    if success == True:
        return HttpResponse(serialized, content_type="application/json")
    else:
        return HttpResponseServerError(serialized, content_type="application/json")


def handler404(request):
    """Display a 404 Page Not Found message."""
    context = {
        'update_timestamp':     fetch_update_datetime(),
        'quote':                fetch_random_quote(),
    }
    response = render(request, 'comparison/404.html', context)
    response.status_code = 404
    return response
