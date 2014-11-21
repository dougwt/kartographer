# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comparison', '0006_auto_20141116_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='KartRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_ip', models.GenericIPAddressField(default=b'0.0.0.0')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('character', models.ForeignKey(to='comparison.Character')),
                ('glider', models.ForeignKey(to='comparison.Glider')),
                ('kart', models.ForeignKey(to='comparison.Kart')),
                ('wheel', models.ForeignKey(to='comparison.Wheel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
