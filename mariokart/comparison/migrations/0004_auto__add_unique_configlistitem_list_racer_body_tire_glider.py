# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'ConfigListItem', fields ['list', 'racer', 'body', 'tire', 'glider']
        db.create_unique(u'comparison_configlistitem', ['list_id', 'racer_id', 'body_id', 'tire_id', 'glider_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'ConfigListItem', fields ['list', 'racer', 'body', 'tire', 'glider']
        db.delete_unique(u'comparison_configlistitem', ['list_id', 'racer_id', 'body_id', 'tire_id', 'glider_id'])


    models = {
        u'comparison.body': {
            'Meta': {'object_name': 'Body'},
            'acceleration': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'handling': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'speed': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'traction': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'})
        },
        u'comparison.configlist': {
            'Meta': {'object_name': 'ConfigList'},
            'create_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'comparison.configlistitem': {
            'Meta': {'unique_together': "(('list', 'racer', 'body', 'tire', 'glider'),)", 'object_name': 'ConfigListItem'},
            'body': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['comparison.Body']"}),
            'glider': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['comparison.Glider']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['comparison.ConfigList']"}),
            'racer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['comparison.Racer']"}),
            'tire': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['comparison.Tire']"})
        },
        u'comparison.glider': {
            'Meta': {'object_name': 'Glider'},
            'acceleration': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'handling': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'speed': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'traction': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'})
        },
        u'comparison.racer': {
            'Meta': {'object_name': 'Racer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'stats': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['comparison.RacerStats']"})
        },
        u'comparison.racerstats': {
            'Meta': {'object_name': 'RacerStats'},
            'acceleration': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'handling': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'speed': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'traction': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'})
        },
        u'comparison.tire': {
            'Meta': {'object_name': 'Tire'},
            'acceleration': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'handling': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'speed': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'traction': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'})
        }
    }

    complete_apps = ['comparison']