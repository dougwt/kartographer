# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comparison', '0009_auto_20141122_0329'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='glider',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='kart',
            options={'ordering': ['pk'], 'verbose_name_plural': 'karts'},
        ),
        migrations.AlterModelOptions(
            name='wheel',
            options={'ordering': ['pk']},
        ),
    ]
