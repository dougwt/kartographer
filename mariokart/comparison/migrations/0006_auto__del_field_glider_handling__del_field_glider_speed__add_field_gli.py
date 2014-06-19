# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Glider.handling'
        db.delete_column(u'comparison_glider', 'handling')

        # Deleting field 'Glider.speed'
        db.delete_column(u'comparison_glider', 'speed')

        # Adding field 'Glider.speed_ground'
        db.add_column(u'comparison_glider', 'speed_ground',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'Glider.speed_water'
        db.add_column(u'comparison_glider', 'speed_water',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'Glider.speed_air'
        db.add_column(u'comparison_glider', 'speed_air',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'Glider.speed_antigravity'
        db.add_column(u'comparison_glider', 'speed_antigravity',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'Glider.handling_ground'
        db.add_column(u'comparison_glider', 'handling_ground',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'Glider.handling_water'
        db.add_column(u'comparison_glider', 'handling_water',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'Glider.handling_air'
        db.add_column(u'comparison_glider', 'handling_air',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'Glider.handling_antigravity'
        db.add_column(u'comparison_glider', 'handling_antigravity',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'Glider.miniturbo'
        db.add_column(u'comparison_glider', 'miniturbo',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Deleting field 'RacerStats.handling'
        db.delete_column(u'comparison_racerstats', 'handling')

        # Deleting field 'RacerStats.speed'
        db.delete_column(u'comparison_racerstats', 'speed')

        # Adding field 'RacerStats.speed_ground'
        db.add_column(u'comparison_racerstats', 'speed_ground',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'RacerStats.speed_water'
        db.add_column(u'comparison_racerstats', 'speed_water',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'RacerStats.speed_air'
        db.add_column(u'comparison_racerstats', 'speed_air',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'RacerStats.speed_antigravity'
        db.add_column(u'comparison_racerstats', 'speed_antigravity',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'RacerStats.handling_ground'
        db.add_column(u'comparison_racerstats', 'handling_ground',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'RacerStats.handling_water'
        db.add_column(u'comparison_racerstats', 'handling_water',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'RacerStats.handling_air'
        db.add_column(u'comparison_racerstats', 'handling_air',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'RacerStats.handling_antigravity'
        db.add_column(u'comparison_racerstats', 'handling_antigravity',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'RacerStats.miniturbo'
        db.add_column(u'comparison_racerstats', 'miniturbo',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Deleting field 'Body.handling'
        db.delete_column(u'comparison_body', 'handling')

        # Deleting field 'Body.speed'
        db.delete_column(u'comparison_body', 'speed')

        # Adding field 'Body.speed_ground'
        db.add_column(u'comparison_body', 'speed_ground',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'Body.speed_water'
        db.add_column(u'comparison_body', 'speed_water',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'Body.speed_air'
        db.add_column(u'comparison_body', 'speed_air',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'Body.speed_antigravity'
        db.add_column(u'comparison_body', 'speed_antigravity',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'Body.handling_ground'
        db.add_column(u'comparison_body', 'handling_ground',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'Body.handling_water'
        db.add_column(u'comparison_body', 'handling_water',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'Body.handling_air'
        db.add_column(u'comparison_body', 'handling_air',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'Body.handling_antigravity'
        db.add_column(u'comparison_body', 'handling_antigravity',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'Body.miniturbo'
        db.add_column(u'comparison_body', 'miniturbo',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Deleting field 'Tire.handling'
        db.delete_column(u'comparison_tire', 'handling')

        # Deleting field 'Tire.speed'
        db.delete_column(u'comparison_tire', 'speed')

        # Adding field 'Tire.speed_ground'
        db.add_column(u'comparison_tire', 'speed_ground',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'Tire.speed_water'
        db.add_column(u'comparison_tire', 'speed_water',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'Tire.speed_air'
        db.add_column(u'comparison_tire', 'speed_air',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'Tire.speed_antigravity'
        db.add_column(u'comparison_tire', 'speed_antigravity',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'Tire.handling_ground'
        db.add_column(u'comparison_tire', 'handling_ground',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'Tire.handling_water'
        db.add_column(u'comparison_tire', 'handling_water',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'Tire.handling_air'
        db.add_column(u'comparison_tire', 'handling_air',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'Tire.handling_antigravity'
        db.add_column(u'comparison_tire', 'handling_antigravity',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'Tire.miniturbo'
        db.add_column(u'comparison_tire', 'miniturbo',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Glider.handling'
        db.add_column(u'comparison_glider', 'handling',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'Glider.speed'
        db.add_column(u'comparison_glider', 'speed',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Deleting field 'Glider.speed_ground'
        db.delete_column(u'comparison_glider', 'speed_ground')

        # Deleting field 'Glider.speed_water'
        db.delete_column(u'comparison_glider', 'speed_water')

        # Deleting field 'Glider.speed_air'
        db.delete_column(u'comparison_glider', 'speed_air')

        # Deleting field 'Glider.speed_antigravity'
        db.delete_column(u'comparison_glider', 'speed_antigravity')

        # Deleting field 'Glider.handling_ground'
        db.delete_column(u'comparison_glider', 'handling_ground')

        # Deleting field 'Glider.handling_water'
        db.delete_column(u'comparison_glider', 'handling_water')

        # Deleting field 'Glider.handling_air'
        db.delete_column(u'comparison_glider', 'handling_air')

        # Deleting field 'Glider.handling_antigravity'
        db.delete_column(u'comparison_glider', 'handling_antigravity')

        # Deleting field 'Glider.miniturbo'
        db.delete_column(u'comparison_glider', 'miniturbo')

        # Adding field 'RacerStats.handling'
        db.add_column(u'comparison_racerstats', 'handling',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'RacerStats.speed'
        db.add_column(u'comparison_racerstats', 'speed',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Deleting field 'RacerStats.speed_ground'
        db.delete_column(u'comparison_racerstats', 'speed_ground')

        # Deleting field 'RacerStats.speed_water'
        db.delete_column(u'comparison_racerstats', 'speed_water')

        # Deleting field 'RacerStats.speed_air'
        db.delete_column(u'comparison_racerstats', 'speed_air')

        # Deleting field 'RacerStats.speed_antigravity'
        db.delete_column(u'comparison_racerstats', 'speed_antigravity')

        # Deleting field 'RacerStats.handling_ground'
        db.delete_column(u'comparison_racerstats', 'handling_ground')

        # Deleting field 'RacerStats.handling_water'
        db.delete_column(u'comparison_racerstats', 'handling_water')

        # Deleting field 'RacerStats.handling_air'
        db.delete_column(u'comparison_racerstats', 'handling_air')

        # Deleting field 'RacerStats.handling_antigravity'
        db.delete_column(u'comparison_racerstats', 'handling_antigravity')

        # Deleting field 'RacerStats.miniturbo'
        db.delete_column(u'comparison_racerstats', 'miniturbo')

        # Adding field 'Body.handling'
        db.add_column(u'comparison_body', 'handling',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'Body.speed'
        db.add_column(u'comparison_body', 'speed',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Deleting field 'Body.speed_ground'
        db.delete_column(u'comparison_body', 'speed_ground')

        # Deleting field 'Body.speed_water'
        db.delete_column(u'comparison_body', 'speed_water')

        # Deleting field 'Body.speed_air'
        db.delete_column(u'comparison_body', 'speed_air')

        # Deleting field 'Body.speed_antigravity'
        db.delete_column(u'comparison_body', 'speed_antigravity')

        # Deleting field 'Body.handling_ground'
        db.delete_column(u'comparison_body', 'handling_ground')

        # Deleting field 'Body.handling_water'
        db.delete_column(u'comparison_body', 'handling_water')

        # Deleting field 'Body.handling_air'
        db.delete_column(u'comparison_body', 'handling_air')

        # Deleting field 'Body.handling_antigravity'
        db.delete_column(u'comparison_body', 'handling_antigravity')

        # Deleting field 'Body.miniturbo'
        db.delete_column(u'comparison_body', 'miniturbo')

        # Adding field 'Tire.handling'
        db.add_column(u'comparison_tire', 'handling',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'Tire.speed'
        db.add_column(u'comparison_tire', 'speed',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Deleting field 'Tire.speed_ground'
        db.delete_column(u'comparison_tire', 'speed_ground')

        # Deleting field 'Tire.speed_water'
        db.delete_column(u'comparison_tire', 'speed_water')

        # Deleting field 'Tire.speed_air'
        db.delete_column(u'comparison_tire', 'speed_air')

        # Deleting field 'Tire.speed_antigravity'
        db.delete_column(u'comparison_tire', 'speed_antigravity')

        # Deleting field 'Tire.handling_ground'
        db.delete_column(u'comparison_tire', 'handling_ground')

        # Deleting field 'Tire.handling_water'
        db.delete_column(u'comparison_tire', 'handling_water')

        # Deleting field 'Tire.handling_air'
        db.delete_column(u'comparison_tire', 'handling_air')

        # Deleting field 'Tire.handling_antigravity'
        db.delete_column(u'comparison_tire', 'handling_antigravity')

        # Deleting field 'Tire.miniturbo'
        db.delete_column(u'comparison_tire', 'miniturbo')


    models = {
        u'comparison.body': {
            'Meta': {'object_name': 'Body'},
            'acceleration': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'handling_air': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'handling_antigravity': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'handling_ground': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'handling_water': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'miniturbo': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'speed_air': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'speed_antigravity': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'speed_ground': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'speed_water': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'traction': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'})
        },
        u'comparison.configlist': {
            'Meta': {'object_name': 'ConfigList'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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
            'handling_air': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'handling_antigravity': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'handling_ground': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'handling_water': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'miniturbo': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'speed_air': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'speed_antigravity': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'speed_ground': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'speed_water': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
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
            'handling_air': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'handling_antigravity': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'handling_ground': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'handling_water': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'miniturbo': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'speed_air': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'speed_antigravity': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'speed_ground': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'speed_water': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'traction': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'})
        },
        u'comparison.tire': {
            'Meta': {'object_name': 'Tire'},
            'acceleration': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'handling_air': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'handling_antigravity': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'handling_ground': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'handling_water': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'miniturbo': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'speed_air': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'speed_antigravity': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'speed_ground': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'speed_water': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'traction': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'})
        }
    }

    complete_apps = ['comparison']