# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Body',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, blank=True)),
                ('speed_ground', models.DecimalField(max_digits=3, decimal_places=2)),
                ('speed_water', models.DecimalField(max_digits=3, decimal_places=2)),
                ('speed_air', models.DecimalField(max_digits=3, decimal_places=2)),
                ('speed_antigravity', models.DecimalField(max_digits=3, decimal_places=2)),
                ('acceleration', models.DecimalField(max_digits=3, decimal_places=2)),
                ('weight', models.DecimalField(max_digits=3, decimal_places=2)),
                ('handling_ground', models.DecimalField(max_digits=3, decimal_places=2)),
                ('handling_water', models.DecimalField(max_digits=3, decimal_places=2)),
                ('handling_air', models.DecimalField(max_digits=3, decimal_places=2)),
                ('handling_antigravity', models.DecimalField(max_digits=3, decimal_places=2)),
                ('traction', models.DecimalField(max_digits=3, decimal_places=2)),
                ('miniturbo', models.DecimalField(max_digits=3, decimal_places=2)),
            ],
            options={
                'verbose_name_plural': 'bodies',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConfigList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=5)),
                ('create_ip', models.GenericIPAddressField(default=b'0.0.0.0')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('view_count', models.PositiveIntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConfigListItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.ForeignKey(to='comparison.Body')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Glider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, blank=True)),
                ('speed_ground', models.DecimalField(max_digits=3, decimal_places=2)),
                ('speed_water', models.DecimalField(max_digits=3, decimal_places=2)),
                ('speed_air', models.DecimalField(max_digits=3, decimal_places=2)),
                ('speed_antigravity', models.DecimalField(max_digits=3, decimal_places=2)),
                ('acceleration', models.DecimalField(max_digits=3, decimal_places=2)),
                ('weight', models.DecimalField(max_digits=3, decimal_places=2)),
                ('handling_ground', models.DecimalField(max_digits=3, decimal_places=2)),
                ('handling_water', models.DecimalField(max_digits=3, decimal_places=2)),
                ('handling_air', models.DecimalField(max_digits=3, decimal_places=2)),
                ('handling_antigravity', models.DecimalField(max_digits=3, decimal_places=2)),
                ('traction', models.DecimalField(max_digits=3, decimal_places=2)),
                ('miniturbo', models.DecimalField(max_digits=3, decimal_places=2)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Racer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RacerStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, blank=True)),
                ('speed_ground', models.DecimalField(max_digits=3, decimal_places=2)),
                ('speed_water', models.DecimalField(max_digits=3, decimal_places=2)),
                ('speed_air', models.DecimalField(max_digits=3, decimal_places=2)),
                ('speed_antigravity', models.DecimalField(max_digits=3, decimal_places=2)),
                ('acceleration', models.DecimalField(max_digits=3, decimal_places=2)),
                ('weight', models.DecimalField(max_digits=3, decimal_places=2)),
                ('handling_ground', models.DecimalField(max_digits=3, decimal_places=2)),
                ('handling_water', models.DecimalField(max_digits=3, decimal_places=2)),
                ('handling_air', models.DecimalField(max_digits=3, decimal_places=2)),
                ('handling_antigravity', models.DecimalField(max_digits=3, decimal_places=2)),
                ('traction', models.DecimalField(max_digits=3, decimal_places=2)),
                ('miniturbo', models.DecimalField(max_digits=3, decimal_places=2)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, blank=True)),
                ('speed_ground', models.DecimalField(max_digits=3, decimal_places=2)),
                ('speed_water', models.DecimalField(max_digits=3, decimal_places=2)),
                ('speed_air', models.DecimalField(max_digits=3, decimal_places=2)),
                ('speed_antigravity', models.DecimalField(max_digits=3, decimal_places=2)),
                ('acceleration', models.DecimalField(max_digits=3, decimal_places=2)),
                ('weight', models.DecimalField(max_digits=3, decimal_places=2)),
                ('handling_ground', models.DecimalField(max_digits=3, decimal_places=2)),
                ('handling_water', models.DecimalField(max_digits=3, decimal_places=2)),
                ('handling_air', models.DecimalField(max_digits=3, decimal_places=2)),
                ('handling_antigravity', models.DecimalField(max_digits=3, decimal_places=2)),
                ('traction', models.DecimalField(max_digits=3, decimal_places=2)),
                ('miniturbo', models.DecimalField(max_digits=3, decimal_places=2)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='racer',
            name='stats',
            field=models.ForeignKey(to='comparison.RacerStats'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='configlistitem',
            name='glider',
            field=models.ForeignKey(to='comparison.Glider'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='configlistitem',
            name='list',
            field=models.ForeignKey(to='comparison.ConfigList'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='configlistitem',
            name='racer',
            field=models.ForeignKey(to='comparison.Racer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='configlistitem',
            name='tire',
            field=models.ForeignKey(to='comparison.Tire'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='configlistitem',
            unique_together=set([('list', 'racer', 'body', 'tire', 'glider')]),
        ),
    ]
