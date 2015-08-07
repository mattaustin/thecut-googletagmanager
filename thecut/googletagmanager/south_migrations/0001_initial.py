# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Container'
        db.create_table(u'googletagmanager_container', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.OneToOneField')(related_name=u'+', unique=True, to=orm['sites.Site'])),
            ('container_id', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('is_enabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'googletagmanager', ['Container'])


    def backwards(self, orm):
        # Deleting model 'Container'
        db.delete_table(u'googletagmanager_container')


    models = {
        u'googletagmanager.container': {
            'Meta': {'ordering': "[u'site']", 'object_name': 'Container'},
            'container_id': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'site': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'+'", 'unique': 'True', 'to': u"orm['sites.Site']"})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['googletagmanager']