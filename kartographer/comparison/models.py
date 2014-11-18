"""Django models for MK8 Kart Comparison Tool."""

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.templatetags.static import static

import re
import uuid
import logging

from ipware.ip import get_ip, get_real_ip

logger = logging.getLogger(__name__)


class KartComponent(models.Model):
    """Abstract model for all kart components."""
    name = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        """Return the component name."""
        return self.name

    def file(self):
        """Return a lowercase form of the name used for image filenames."""
        return re.sub(ur'[\W_]+', u'', self.name.lower(), flags=re.UNICODE)

    class Meta:
        abstract = True


class CommonStats(KartComponent):
    """Common stats across all kart components."""
    speed_ground = models.DecimalField(max_digits=3, decimal_places=2)
    speed_water = models.DecimalField(max_digits=3, decimal_places=2)
    speed_air = models.DecimalField(max_digits=3, decimal_places=2)
    speed_antigravity = models.DecimalField(max_digits=3, decimal_places=2)
    acceleration = models.DecimalField(max_digits=3, decimal_places=2)
    weight = models.DecimalField(max_digits=3, decimal_places=2)
    handling_ground = models.DecimalField(max_digits=3, decimal_places=2)
    handling_water = models.DecimalField(max_digits=3, decimal_places=2)
    handling_air = models.DecimalField(max_digits=3, decimal_places=2)
    handling_antigravity = models.DecimalField(max_digits=3, decimal_places=2)
    traction = models.DecimalField(max_digits=3, decimal_places=2)
    miniturbo = models.DecimalField(max_digits=3, decimal_places=2)

    class Meta:
        abstract = True


class CharacterStats(CommonStats):
    """Maps racers to the stats belonging to the 9 weight subclasses."""
    sort_order = models.CharField(max_length=5)


class Kart(CommonStats):
    """Stats for a kart body."""

    def file(self):
        """Return a lowercase form of the name used for image filenames."""
        return static('images/mk8/karts/%s.png' % super(Kart, self).file())

    class Meta:
        verbose_name_plural = "karts"


class Wheel(CommonStats):
    """Stats for a set of kart wheels."""

    def file(self):
        """Return a lowercase form of the name used for image filenames."""
        return static('images/mk8/wheels/%s.png' % super(Wheel, self).file())


class Glider(CommonStats):

    """Stats for a kart glider."""

    def file(self):
        """Return a lowercase form of the name used for image filenames."""
        return static('images/mk8/gliders/%s.png' % super(Glider, self).file())


class Character(KartComponent):
    """Stats for a kart racer/driver."""
    stats = models.ForeignKey(CharacterStats)

    def file(self):
        """Return a lowercase form of the name used for image filenames."""
        return static('images/mk8/faces/%s.png' % super(Character, self).file())


class KartConfig():
    """Stats for a complete kart configuration."""

    def __init__(self, (character_id, kart_id, wheel_id, glider_id)):
        """Create a config with the supplied component ids."""
        try:
            self.character = Character.objects.get(pk=character_id)
            self.kart = Kart.objects.get(pk=kart_id)
            self.wheel = Wheel.objects.get(pk=wheel_id)
            self.glider = Glider.objects.get(pk=glider_id)
            self.valid = True

            self.speed_ground = \
                self.character.stats.speed_ground + \
                self.kart.speed_ground + \
                self.wheel.speed_ground + \
                self.glider.speed_ground

            self.speed_water = \
                self.character.stats.speed_water + \
                self.kart.speed_water + \
                self.wheel.speed_water + \
                self.glider.speed_water

            self.speed_air = \
                self.character.stats.speed_air + \
                self.kart.speed_air + \
                self.wheel.speed_air + \
                self.glider.speed_air

            self.speed_antigravity = \
                self.character.stats.speed_antigravity + \
                self.kart.speed_antigravity + \
                self.wheel.speed_antigravity + \
                self.glider.speed_antigravity

            self.acceleration = \
                self.character.stats.acceleration + \
                self.kart.acceleration + \
                self.wheel.acceleration + \
                self.glider.acceleration

            self.weight = \
                self.character.stats.weight + \
                self.kart.weight + \
                self.wheel.weight + \
                self.glider.weight

            self.handling_ground = \
                self.character.stats.handling_ground + \
                self.kart.handling_ground + \
                self.wheel.handling_ground + \
                self.glider.handling_ground

            self.handling_water = \
                self.character.stats.handling_water + \
                self.kart.handling_water + \
                self.wheel.handling_water + \
                self.glider.handling_water

            self.handling_air = \
                self.character.stats.handling_air + \
                self.kart.handling_air + \
                self.wheel.handling_air + \
                self.glider.handling_air

            self.handling_antigravity = \
                self.character.stats.handling_antigravity + \
                self.kart.handling_antigravity + \
                self.wheel.handling_antigravity + \
                self.glider.handling_antigravity

            self.traction = \
                self.character.stats.traction + \
                self.kart.traction + \
                self.wheel.traction + \
                self.glider.traction

            self.miniturbo = \
                self.character.stats.miniturbo + \
                self.kart.miniturbo + \
                self.wheel.miniturbo + \
                self.glider.miniturbo

        except ObjectDoesNotExist:
            self.valid = False


class ConfigList(models.Model):
    """A saved kart configuration list associated with a url hash."""
    URL_LENGTH = 5
    url = models.CharField(max_length=URL_LENGTH)
    create_ip = models.GenericIPAddressField(default='0.0.0.0')
    create_date = models.DateTimeField(auto_now_add=True)
    view_count = models.PositiveIntegerField(default=0)

    @classmethod
    def create(cls, request):
        """Initialize a ConfigList with visitor's IP and generated url hash."""
        ip = get_real_ip(request)
        if ip is None:
            ip = get_ip(request)
            if ip is None:
                ip = '111.111.111.111'

        url = cls.generate_url(cls.URL_LENGTH)
        list = cls(url=url, create_ip=ip)

        logger.info('Adding ConfigList \'%s\' (%s)' % (url, ip))

        return list

    @staticmethod
    def generate_url(length):
        """Generate a unique url hash."""
        while True:
            url_hash = uuid.uuid4().hex[0:length]
            try:
                ConfigList.objects.get(url=url_hash)
                break
            except ObjectDoesNotExist:
                return url_hash

    def __unicode__(self):
        """Display url hash to id mapping."""
        return '[\'%s\' -> %s]' % (self.url, self.id)


class ConfigListItem(models.Model):
    """A saved kart configuration associated with a ConfigList."""
    list = models.ForeignKey(ConfigList)
    character = models.ForeignKey(Character)
    kart = models.ForeignKey(Kart)
    wheel = models.ForeignKey(Wheel)
    glider = models.ForeignKey(Glider)

    @classmethod
    def create(cls, list, character, kart, wheel, glider):
        """Initialize ConfigListItem with default parameters order."""
        logger.info('Adding \'%s\' ConfigListItem [%s, %s, %s, %s]' %
                    (list.url, character, kart, wheel, glider))
        return cls(list=list, character=character, kart=kart, wheel=wheel, glider=glider)

    class Meta:
        unique_together = ("list", "character", "kart", "wheel", "glider")
