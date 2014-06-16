# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ConfigList.name'
        db.delete_column(u'comparison_configlist', 'name')

        # Deleting field 'ConfigListItem.name'
        db.delete_column(u'comparison_configlistitem', 'name')


    def backwards(self, orm):
        # Adding field 'ConfigList.name'
        db.add_column(u'comparison_configlist', 'name',
                      self.gf('django.db.models.fields.CharField')(default='temp', max_length=30),
                      keep_default=False)

        # Adding field 'ConfigListItem.name'
        db.add_column(u'comparison_configlistitem', 'name',
                      self.gf('django.db.models.fields.CharField')(default='temp', max_length=30),
                      keep_default=False)


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
        u'comparison.configlist': {
            'Meta': {'object_name': 'ConfigList'},
            'create_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'comparison.configlistitem': {
            'Meta': {'object_name': 'ConfigListItem'},
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