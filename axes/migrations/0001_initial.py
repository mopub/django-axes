# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AccessAttempt'
        db.create_table(u'axes_accessattempt', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_agent', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('trusted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('get_data', self.gf('django.db.models.fields.TextField')()),
            ('post_data', self.gf('django.db.models.fields.TextField')()),
            ('http_accept', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('path_info', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('failures_since_start', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('attempt_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'axes', ['AccessAttempt'])


    def backwards(self, orm):
        # Deleting model 'AccessAttempt'
        db.delete_table(u'axes_accessattempt')


    models = {
        u'axes.accessattempt': {
            'Meta': {'ordering': "['-attempt_time']", 'object_name': 'AccessAttempt'},
            'attempt_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'failures_since_start': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'get_data': ('django.db.models.fields.TextField', [], {}),
            'http_accept': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True'}),
            'path_info': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'post_data': ('django.db.models.fields.TextField', [], {}),
            'trusted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        }
    }

    complete_apps = ['axes']
