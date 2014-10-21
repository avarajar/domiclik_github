# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AdiUnicoTres'
        db.create_table(u'Administrador_adiunicotres', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('precio', self.gf('django.db.models.fields.IntegerField')()),
            ('restaurant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Administrador.Restaurante'])),
            ('menuesp', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['Administrador.Menuesp'])),
            ('titulo', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['Administrador.TituloAdicionale'])),
        ))
        db.send_create_signal(u'Administrador', ['AdiUnicoTres'])

        # Adding model 'AdicionalTres'
        db.create_table(u'Administrador_adicionaltres', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('precio', self.gf('django.db.models.fields.IntegerField')()),
            ('restaurant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Administrador.Restaurante'])),
            ('menuesp', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['Administrador.Menuesp'])),
            ('titulo', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['Administrador.TituloAdicionale'])),
        ))
        db.send_create_signal(u'Administrador', ['AdicionalTres'])

        # Adding model 'AdiUnicoDos'
        db.create_table(u'Administrador_adiunicodos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('precio', self.gf('django.db.models.fields.IntegerField')()),
            ('restaurant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Administrador.Restaurante'])),
            ('menuesp', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['Administrador.Menuesp'])),
            ('titulo', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['Administrador.TituloAdicionale'])),
        ))
        db.send_create_signal(u'Administrador', ['AdiUnicoDos'])

        # Adding model 'AdicionalDos'
        db.create_table(u'Administrador_adicionaldos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('precio', self.gf('django.db.models.fields.IntegerField')()),
            ('restaurant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Administrador.Restaurante'])),
            ('menuesp', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['Administrador.Menuesp'])),
            ('titulo', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['Administrador.TituloAdicionale'])),
        ))
        db.send_create_signal(u'Administrador', ['AdicionalDos'])


    def backwards(self, orm):
        # Deleting model 'AdiUnicoTres'
        db.delete_table(u'Administrador_adiunicotres')

        # Deleting model 'AdicionalTres'
        db.delete_table(u'Administrador_adicionaltres')

        # Deleting model 'AdiUnicoDos'
        db.delete_table(u'Administrador_adiunicodos')

        # Deleting model 'AdicionalDos'
        db.delete_table(u'Administrador_adicionaldos')


    models = {
        u'Administrador.adicionaldos': {
            'Meta': {'object_name': 'AdicionalDos'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menuesp': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['Administrador.Menuesp']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'precio': ('django.db.models.fields.IntegerField', [], {}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Administrador.Restaurante']"}),
            'titulo': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['Administrador.TituloAdicionale']"})
        },
        u'Administrador.adicionale': {
            'Meta': {'object_name': 'Adicionale'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menuesp': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['Administrador.Menuesp']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'precio': ('django.db.models.fields.IntegerField', [], {}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Administrador.Restaurante']"}),
            'titulo': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['Administrador.TituloAdicionale']"})
        },
        u'Administrador.adicionaltres': {
            'Meta': {'object_name': 'AdicionalTres'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menuesp': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['Administrador.Menuesp']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'precio': ('django.db.models.fields.IntegerField', [], {}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Administrador.Restaurante']"}),
            'titulo': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['Administrador.TituloAdicionale']"})
        },
        u'Administrador.adiunico': {
            'Meta': {'object_name': 'AdiUnico'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menuesp': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['Administrador.Menuesp']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'precio': ('django.db.models.fields.IntegerField', [], {}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Administrador.Restaurante']"}),
            'titulo': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['Administrador.TituloAdicionale']"})
        },
        u'Administrador.adiunicodos': {
            'Meta': {'object_name': 'AdiUnicoDos'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menuesp': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['Administrador.Menuesp']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'precio': ('django.db.models.fields.IntegerField', [], {}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Administrador.Restaurante']"}),
            'titulo': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['Administrador.TituloAdicionale']"})
        },
        u'Administrador.adiunicotres': {
            'Meta': {'object_name': 'AdiUnicoTres'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menuesp': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['Administrador.Menuesp']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'precio': ('django.db.models.fields.IntegerField', [], {}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Administrador.Restaurante']"}),
            'titulo': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['Administrador.TituloAdicionale']"})
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
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'Administrador.menuesp': {
            'Meta': {'object_name': 'Menuesp'},
            'categoria': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['Administrador.Categoria']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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
            'sector': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Administrador.Sectore']", 'symmetrical': 'False'}),
            'tipo': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Administrador.Tipo']", 'symmetrical': 'False'})
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
            'menuesp': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['Administrador.Menuesp']"}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Administrador.Restaurante']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'})
        }
    }

    complete_apps = ['Administrador']