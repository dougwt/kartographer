from django.db import models

# Create your models here.
class BaseModel(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    def filename(self):
        name = self.name.lower()
        return name.translate(name.maketrans("",""), string.punctuation)

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

class Body(CommonStats):
    pass

class Tire(CommonStats):
    pass

class Glider(CommonStats):
    pass

class Racer(BaseModel):
    stats = models.ForeignKey(RacerStats)
