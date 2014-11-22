# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comparison', '0008_auto_20141122_0223'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='character',
            options={'ordering': ['pk']},
        ),
    ]
