# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RacerStats'
        db.create_table(u'comparison_racerstats', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('speed', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
            ('acceleration', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
            ('weight', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
            ('handling', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
            ('traction', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
        ))
        db.send_create_signal(u'comparison', ['RacerStats'])

        # Adding model 'Body'
        db.create_table(u'comparison_body', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('speed', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
            ('acceleration', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
            ('weight', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
            ('handling', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
            ('traction', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
        ))
        db.send_create_signal(u'comparison', ['Body'])

        # Adding model 'Tire'
        db.create_table(u'comparison_tire', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('speed', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
            ('acceleration', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
            ('weight', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
            ('handling', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
            ('traction', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
        ))
        db.send_create_signal(u'comparison', ['Tire'])

        # Adding model 'Glider'
        db.create_table(u'comparison_glider', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('speed', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
            ('acceleration', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
            ('weight', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
            ('handling', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
            ('traction', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
        ))
        db.send_create_signal(u'comparison', ['Glider'])

        # Adding model 'Racer'
        db.create_table(u'comparison_racer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('stats', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['comparison.RacerStats'])),
        ))
        db.send_create_signal(u'comparison', ['Racer'])


    def backwards(self, orm):
        # Deleting model 'RacerStats'
        db.delete_table(u'comparison_racerstats')

        # Deleting model 'Body'
        db.delete_table(u'comparison_body')

        # Deleting model 'Tire'
        db.delete_table(u'comparison_tire')

        # Deleting model 'Glider'
        db.delete_table(u'comparison_glider')

        # Deleting model 'Racer'
        db.delete_table(u'comparison_racer')


    models = {
        u'comparison.body': {
            'Meta': {'object_name': 'Body'},
            'acceleration': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'handling': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'speed': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'traction': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'})
        },
        u'comparison.glider': {
            'Meta': {'object_name': 'Glider'},
            'acceleration': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'handling': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'speed': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'traction': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'})
        },
        u'comparison.racer': {
            'Meta': {'object_name': 'Racer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'stats': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['comparison.RacerStats']"})
        },
        u'comparison.racerstats': {
            'Meta': {'object_name': 'RacerStats'},
            'acceleration': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'handling': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'speed': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'traction': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'})
        },
        u'comparison.tire': {
            'Meta': {'object_name': 'Tire'},
            'acceleration': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'handling': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'speed': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'traction': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'})
        }
    }

    complete_apps = ['comparison']