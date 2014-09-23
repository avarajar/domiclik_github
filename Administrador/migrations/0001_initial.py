# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ciudade'
        db.create_table(u'Administrador_ciudade', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'Administrador', ['Ciudade'])

        # Adding model 'Sectore'
        db.create_table(u'Administrador_sectore', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'Administrador', ['Sectore'])

        # Adding model 'Tipo'
        db.create_table(u'Administrador_tipo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'Administrador', ['Tipo'])

        # Adding model 'Restaurante'
        db.create_table(u'Administrador_restaurante', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(default='descripcion', blank=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('ciudad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Administrador.Ciudade'])),
            ('sector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Administrador.Sectore'])),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Administrador.Tipo'])),
            ('hora_abrir', self.gf('django.db.models.fields.TimeField')()),
            ('hora_cerrar', self.gf('django.db.models.fields.TimeField')()),
            ('precio_domicilio', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'Administrador', ['Restaurante'])

        # Adding model 'Menu'
        db.create_table(u'Administrador_menu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('restaurant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Administrador.Restaurante'])),
        ))
        db.send_create_signal(u'Administrador', ['Menu'])

        # Adding model 'Menuesp'
        db.create_table(u'Administrador_menuesp', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('precio', self.gf('django.db.models.fields.IntegerField')()),
            ('menu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Administrador.Menu'])),
            ('restaurant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Administrador.Restaurante'])),
        ))
        db.send_create_signal(u'Administrador', ['Menuesp'])

        # Adding model 'Tamano'
        db.create_table(u'Administrador_tamano', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tamano', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('precio', self.gf('django.db.models.fields.IntegerField')()),
            ('menuesp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Administrador.Menuesp'])),
        ))
        db.send_create_signal(u'Administrador', ['Tamano'])

        # Adding model 'Adicionale'
        db.create_table(u'Administrador_adicionale', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('precio', self.gf('django.db.models.fields.IntegerField')()),
            ('menuesp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Administrador.Menuesp'])),
        ))
        db.send_create_signal(u'Administrador', ['Adicionale'])


    def backwards(self, orm):
        # Deleting model 'Ciudade'
        db.delete_table(u'Administrador_ciudade')

        # Deleting model 'Sectore'
        db.delete_table(u'Administrador_sectore')

        # Deleting model 'Tipo'
        db.delete_table(u'Administrador_tipo')

        # Deleting model 'Restaurante'
        db.delete_table(u'Administrador_restaurante')

        # Deleting model 'Menu'
        db.delete_table(u'Administrador_menu')

        # Deleting model 'Menuesp'
        db.delete_table(u'Administrador_menuesp')

        # Deleting model 'Tamano'
        db.delete_table(u'Administrador_tamano')

        # Deleting model 'Adicionale'
        db.delete_table(u'Administrador_adicionale')


    models = {
        u'Administrador.adicionale': {
            'Meta': {'object_name': 'Adicionale'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menuesp': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Administrador.Menuesp']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'precio': ('django.db.models.fields.IntegerField', [], {})
        },
        u'Administrador.ciudade': {
            'Meta': {'object_name': 'Ciudade'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'Administrador.menu': {
            'Meta': {'object_name': 'Menu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Administrador.Restaurante']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'Administrador.menuesp': {
            'Meta': {'object_name': 'Menuesp'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Administrador.Menu']"}),
            'precio': ('django.db.models.fields.IntegerField', [], {}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Administrador.Restaurante']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'Administrador.restaurante': {
            'Meta': {'object_name': 'Restaurante'},
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Administrador.Ciudade']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "'descripcion'", 'blank': 'True'}),
            'hora_abrir': ('django.db.models.fields.TimeField', [], {}),
            'hora_cerrar': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'precio_domicilio': ('django.db.models.fields.IntegerField', [], {}),
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Administrador.Sectore']"}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Administrador.Tipo']"})
        },
        u'Administrador.sectore': {
            'Meta': {'object_name': 'Sectore'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'Administrador.tamano': {
            'Meta': {'object_name': 'Tamano'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menuesp': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Administrador.Menuesp']"}),
            'precio': ('django.db.models.fields.IntegerField', [], {}),
            'tamano': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'})
        },
        u'Administrador.tipo': {
            'Meta': {'object_name': 'Tipo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['Administrador']