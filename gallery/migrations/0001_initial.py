# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Album'
        db.create_table(u'gallery_album', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('main', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'gallery', ['Album'])

        # Adding model 'Image'
        db.create_table(u'gallery_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['gallery.Album'])),
        ))
        db.send_create_signal(u'gallery', ['Image'])

    def backwards(self, orm):
        # Deleting model 'Album'
        db.delete_table(u'gallery_album')

        # Deleting model 'Image'
        db.delete_table(u'gallery_image')

    models = {
        u'gallery.album': {
            'Meta': {'object_name': 'Album'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.SlugField', [], {'max_length': '255'})
        },
        u'gallery.image': {
            'Meta': {'object_name': 'Image'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['gallery.Album']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['gallery']