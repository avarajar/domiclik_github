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

        # Adding model 'Categoria'
        db.create_table(u'Administrador_categoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('imagen_categoria', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('restaurant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Administrador.Restaurante'])),
        ))
        db.send_create_signal(u'Administrador', ['Categoria'])

        # Adding model 'Menuesp'
        db.create_table(u'Administrador_menuesp', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('precio', self.gf('django.db.models.fields.IntegerField')()),
            ('restaurant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Administrador.Restaurante'])),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Administrador.Categoria'])),
        ))
        db.send_create_signal(u'Administrador', ['Menuesp'])

        # Adding model 'TituloAdicionale'
        db.create_table(u'Administrador_tituloadicionale', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('menuesp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Administrador.Menuesp'])),
        ))
        db.send_create_signal(u'Administrador', ['TituloAdicionale'])

        # Adding model 'AdiUnico'
        db.create_table(u'Administrador_adiunico', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('precio', self.gf('django.db.models.fields.IntegerField')()),
            ('menuesp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Administrador.Menuesp'])),
        ))
        db.send_create_signal(u'Administrador', ['AdiUnico'])

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

        # Deleting model 'Categoria'
        db.delete_table(u'Administrador_categoria')

        # Deleting model 'Menuesp'
        db.delete_table(u'Administrador_menuesp')

        # Deleting model 'TituloAdicionale'
        db.delete_table(u'Administrador_tituloadicionale')

        # Deleting model 'AdiUnico'
        db.delete_table(u'Administrador_adiunico')

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
        u'Administrador.adiunico': {
            'Meta': {'object_name': 'AdiUnico'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menuesp': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Administrador.Menuesp']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'precio': ('django.db.models.fields.IntegerField', [], {})
        },
        u'Administrador.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen_categoria': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Administrador.Restaurante']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'Administrador.ciudade': {
            'Meta': {'object_name': 'Ciudade'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'Administrador.menuesp': {
            'Meta': {'object_name': 'Menuesp'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Administrador.Categoria']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
        u'Administrador.tipo': {
            'Meta': {'object_name': 'Tipo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'Administrador.tituloadicionale': {
            'Meta': {'object_name': 'TituloAdicionale'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menuesp': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Administrador.Menuesp']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'})
        }
    }

    complete_apps = ['Administrador']