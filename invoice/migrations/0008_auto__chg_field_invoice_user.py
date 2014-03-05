# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from django.conf import settings


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Invoice.user'
        db.alter_column(u'invoice_invoice', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm[settings.AUTH_USER_MODEL]))

    def backwards(self, orm):

        # Changing field 'Invoice.user'
        db.alter_column(u'invoice_invoice', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

    models = {
        u'accounts.user': {
            'Meta': {'object_name': 'User'},
            'addresses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['addressbook.Address']", 'symmetrical': 'False'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "u'en'", 'max_length': '5'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'addressbook.address': {
            'Meta': {'ordering': "['created']", 'object_name': 'Address'},
            'address_one': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'address_two': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['addressbook.Country']"}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'addressbook.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'invoice.currency': {
            'Meta': {'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_symbol': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'pre_symbol': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        },
        u'invoice.invoice': {
            'Meta': {'ordering': "('-invoice_date', 'id')", 'object_name': 'Invoice'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'invoice_set'", 'to': u"orm['addressbook.Address']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['invoice.Currency']", 'null': 'True', 'blank': 'True'}),
            'draft': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'invoice_id': ('django.db.models.fields.CharField', [], {'max_length': '6', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'invoiced': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'paid_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.User']"})
        },
        u'invoice.invoiceitem': {
            'Meta': {'object_name': 'InvoiceItem'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': u"orm['invoice.Invoice']"}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'default': '1', 'max_digits': '8', 'decimal_places': '2'}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'})
        }
    }

    complete_apps = ['invoice']
