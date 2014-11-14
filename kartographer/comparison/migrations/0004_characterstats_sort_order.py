# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comparison', '0003_auto_20141114_0147'),
    ]

    operations = [
        migrations.AddField(
            model_name='characterstats',
            name='sort_order',
            field=models.CharField(default='d', max_length=5),
            preserve_default=False,
        ),
    ]
