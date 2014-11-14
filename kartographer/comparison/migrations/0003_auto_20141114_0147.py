# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comparison', '0002_auto_20141113_1737'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kart',
            options={'verbose_name_plural': 'karts'},
        ),
    ]
