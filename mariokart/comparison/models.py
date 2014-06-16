from django.db import models
from django.templatetags.static import static
from django.core.exceptions import ObjectDoesNotExist

import re
import uuid

# Create your models here.
class BaseModel(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    def file(self):
        return re.sub(ur'[\W_]+', u'', self.name.lower(), flags=re.UNICODE)

    class Meta:
        abstract = True

class CommonStats(BaseModel):
    speed = models.DecimalField(max_digits=3, decimal_places=2)
    acceleration = models.DecimalField(max_digits=3, decimal_places=2)
    weight = models.DecimalField(max_digits=3, decimal_places=2)
    handling = models.DecimalField(max_digits=3, decimal_places=2)
    traction = models.DecimalField(max_digits=3, decimal_places=2)

    class Meta:
        abstract = True

class RacerStats(CommonStats):
    pass

    def file(self):
        # return '%s.png' % super(RacerStats, self).file()
        return ''

class Body(CommonStats):
    pass

    def file(self):
        return static('mk8/bodies/%s.png' % super(Body, self).file())

    class Meta:
        verbose_name_plural = "bodies"

class Tire(CommonStats):
    pass

    def file(self):
        return static('mk8/tires/%s.png' % super(Tire, self).file())

class Glider(CommonStats):
    pass

    def file(self):
        return static('mk8/gliders/%s.png' % super(Glider, self).file())

class Racer(BaseModel):
    stats = models.ForeignKey(RacerStats)

    def file(self):
        return static('mk8/racers/%s.png' % super(Racer, self).file())

class KartConfig():
    def __init__(self, (racer_id, body_id, tire_id, glider_id)):
        try:
            self.racer = Racer.objects.get(pk=racer_id)
            self.body = Body.objects.get(pk=body_id)
            self.tire = Tire.objects.get(pk=tire_id)
            self.glider = Glider.objects.get(pk=glider_id)
            self.valid = True

            self.speed = self.racer.stats.speed + self.body.speed + self.tire.speed + self.glider.speed
            self.acceleration = self.racer.stats.acceleration + self.body.acceleration + self.tire.acceleration + self.glider.acceleration
            self.weight = self.racer.stats.weight + self.body.weight + self.tire.weight + self.glider.weight
            self.handling = self.racer.stats.handling + self.body.handling + self.tire.handling + self.glider.handling
            self.traction = self.racer.stats.traction + self.body.traction + self.tire.traction + self.glider.traction

        except ObjectDoesNotExist:
            self.valid = False

class ConfigList(BaseModel):
    URL_LENGTH = 5
    url =  = models.CharField(max_length=URL_LENGTH)
    create_date = models.DateField(auto_now_add=True)

    def __init__(self):
        self.url = generate_url(self.URL_LENGTH)

    def __init__(config_list):
        pass

    def generate_url(self, length):
        while True:
            url_hash = uuid.uuid4()[0:length]
            try:
                ConfigList.objects.get(url=url_hash):
                break
            except ObjectDoesNotExist:
                return url_hash

class ConfigListItem(BaseModel):
    list = models.ForeignKey(ConfigList)
    racer = models.ForeignKey(Racer)
    body = models.ForeignKey(Body)
    tire = models.ForeignKey(Tire)
    glider = models.ForeignKey(Glider)

    def __init__(self, racer, body, tire, glider):
        self.racer = racer
        self.body = body
        self.tire = tire
        self.glider = glider
