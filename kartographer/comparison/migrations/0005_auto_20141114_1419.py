# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comparison', '0004_characterstats_sort_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='character',
            options={'ordering': ['stats']},
        ),
        migrations.AlterModelOptions(
            name='characterstats',
            options={'ordering': ['sort_order']},
        ),
    ]
