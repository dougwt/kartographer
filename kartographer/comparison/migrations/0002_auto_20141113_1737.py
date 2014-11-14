# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comparison', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Racer',
            new_name='Character',
        ),
        migrations.RenameModel(
            old_name='RacerStats',
            new_name='CharacterStats',
        ),
        migrations.RenameModel(
            old_name='Body',
            new_name='Kart',
        ),
        migrations.RenameModel(
            old_name='Tire',
            new_name='Wheel',
        ),
        migrations.RenameField(
            model_name='configlistitem',
            old_name='racer',
            new_name='character',
        ),
        migrations.RenameField(
            model_name='configlistitem',
            old_name='body',
            new_name='kart',
        ),
        migrations.RenameField(
            model_name='configlistitem',
            old_name='tire',
            new_name='wheel',
        ),
        migrations.AlterUniqueTogether(
            name='configlistitem',
            unique_together=set([('list', 'character', 'kart', 'wheel', 'glider')]),
        ),
    ]
