"""Django models for MK8 Kart Comparison Tool."""

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.templatetags.static import static

import re
import uuid

from ipware.ip import get_ip, get_real_ip


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


class RacerStats(CommonStats):
    """Maps racers to the stats belonging to the 7 weight subclasses."""
    pass


class Body(CommonStats):
    """Stats for a kart body."""

    def file(self):
        """Return a lowercase form of the name used for image filenames."""
        return static('mk8/bodies/%s.png' % super(Body, self).file())

    class Meta:
        verbose_name_plural = "bodies"


class Tire(CommonStats):
    """Stats for a set of kart tires."""

    def file(self):
        """Return a lowercase form of the name used for image filenames."""
        return static('mk8/tires/%s.png' % super(Tire, self).file())


class Glider(CommonStats):

    """Stats for a kart glider."""

    def file(self):
        """Return a lowercase form of the name used for image filenames."""
        return static('mk8/gliders/%s.png' % super(Glider, self).file())


class Racer(KartComponent):
    """Stats for a kart racer/driver."""
    stats = models.ForeignKey(RacerStats)

    def file(self):
        """Return a lowercase form of the name used for image filenames."""
        return static('mk8/racers/%s.png' % super(Racer, self).file())


class KartConfig():
    """Stats for a complete kart configuration."""

    def __init__(self, (racer_id, body_id, tire_id, glider_id)):
        """Create a config with the supplied component ids."""
        try:
            self.racer = Racer.objects.get(pk=racer_id)
            self.body = Body.objects.get(pk=body_id)
            self.tire = Tire.objects.get(pk=tire_id)
            self.glider = Glider.objects.get(pk=glider_id)
            self.valid = True

            self.speed_ground = \
                self.racer.stats.speed_ground + \
                self.body.speed_ground + \
                self.tire.speed_ground + \
                self.glider.speed_ground

            self.speed_water = \
                self.racer.stats.speed_water + \
                self.body.speed_water + \
                self.tire.speed_water + \
                self.glider.speed_water

            self.speed_air = \
                self.racer.stats.speed_air + \
                self.body.speed_air + \
                self.tire.speed_air + \
                self.glider.speed_air

            self.speed_antigravity = \
                self.racer.stats.speed_antigravity + \
                self.body.speed_antigravity + \
                self.tire.speed_antigravity + \
                self.glider.speed_antigravity

            self.acceleration = \
                self.racer.stats.acceleration + \
                self.body.acceleration + \
                self.tire.acceleration + \
                self.glider.acceleration

            self.weight = \
                self.racer.stats.weight + \
                self.body.weight + \
                self.tire.weight + \
                self.glider.weight

            self.handling_ground = \
                self.racer.stats.handling_ground + \
                self.body.handling_ground + \
                self.tire.handling_ground + \
                self.glider.handling_ground

            self.handling_water = \
                self.racer.stats.handling_water + \
                self.body.handling_water + \
                self.tire.handling_water + \
                self.glider.handling_water

            self.handling_air = \
                self.racer.stats.handling_air + \
                self.body.handling_air + \
                self.tire.handling_air + \
                self.glider.handling_air

            self.handling_antigravity = \
                self.racer.stats.handling_antigravity + \
                self.body.handling_antigravity + \
                self.tire.handling_antigravity + \
                self.glider.handling_antigravity

            self.traction = \
                self.racer.stats.traction + \
                self.body.traction + \
                self.tire.traction + \
                self.glider.traction

            self.miniturbo = \
                self.racer.stats.miniturbo + \
                self.body.miniturbo + \
                self.tire.miniturbo + \
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
    racer = models.ForeignKey(Racer)
    body = models.ForeignKey(Body)
    tire = models.ForeignKey(Tire)
    glider = models.ForeignKey(Glider)

    @classmethod
    def create(cls, list, racer, body, tire, glider):
        """Initialize ConfigListItem with default parameters order."""
        return cls(list=list, racer=racer, body=body, tire=tire, glider=glider)

    class Meta:
        unique_together = ("list", "racer", "body", "tire", "glider")
