# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Race'
        db.create_table('races_race', (
            ('cut_off', self.gf('django.db.models.fields.CharField')(max_length=75, null=True, blank=True)),
            ('entry_form', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('lodging', self.gf('django.db.models.fields.URLField')(default='http://', max_length=200, null=True, blank=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unit', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('discounts', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['members.Member'])),
            ('location', self.gf('django.db.models.fields.TextField')()),
            ('start_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('map_link', self.gf('django.db.models.fields.URLField')(default='http://', max_length=200)),
            ('awards', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('reg_url', self.gf('django.db.models.fields.URLField')(default='http://', max_length=200, null=True, blank=True)),
            ('distance', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=10)),
            ('course_map', self.gf('django.db.models.fields.URLField')(default='http://', max_length=200, null=True, blank=True)),
            ('slogan', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('packet_pickup', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('annual', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('race_type', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('reg_description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('races', ['Race'])

        # Adding model 'Registration'
        db.create_table('races_registration', (
            ('reg_date', self.gf('django.db.models.fields.DateField')()),
            ('reg_cost', self.gf('django.db.models.fields.IntegerField')()),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['races.Race'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('races', ['Registration'])

        # Adding model 'News'
        db.create_table('races_news', (
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['races.Race'])),
            ('draft', self.gf('django.db.models.fields.IntegerField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
        ))
        db.send_create_signal('races', ['News'])

        # Adding model 'EmergencyContact'
        db.create_table('races_emergencycontact', (
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('relationship', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('races', ['EmergencyContact'])

        # Adding model 'Racer'
        db.create_table('races_racer', (
            ('city', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('gender', self.gf('django.db.models.fields.IntegerField')()),
            ('trailhawk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['members.Member'], unique=True, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['races.EmergencyContact'], null=True, blank=True)),
            ('shirt_size', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('birth_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('races', ['Racer'])

        # Adding model 'Result'
        db.create_table('races_result', (
            ('course_record', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('racer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['races.Racer'])),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['races.Race'])),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('time', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=20, null=True, blank=True)),
            ('bib_number', self.gf('django.db.models.fields.IntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dq', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
        ))
        db.send_create_signal('races', ['Result'])

        # Adding model 'Report'
        db.create_table('races_report', (
            ('report', self.gf('django.db.models.fields.URLField')(default='http://', max_length=200)),
            ('racer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['races.Racer'])),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['races.Race'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('races', ['Report'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Race'
        db.delete_table('races_race')

        # Deleting model 'Registration'
        db.delete_table('races_registration')

        # Deleting model 'News'
        db.delete_table('races_news')

        # Deleting model 'EmergencyContact'
        db.delete_table('races_emergencycontact')

        # Deleting model 'Racer'
        db.delete_table('races_racer')

        # Deleting model 'Result'
        db.delete_table('races_result')

        # Deleting model 'Report'
        db.delete_table('races_report')
    
    
    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'members.member': {
            'Meta': {'object_name': 'Member'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'address': ('django.db.models.fields.TextField', [], {}),
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date_paid': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'hawk_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'member_since': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'races.emergencycontact': {
            'Meta': {'object_name': 'EmergencyContact'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'races.news': {
            'Meta': {'object_name': 'News'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'draft': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['races.Race']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'races.race': {
            'Meta': {'object_name': 'Race'},
            'annual': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'awards': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['members.Member']"}),
            'course_map': ('django.db.models.fields.URLField', [], {'default': "'http://'", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'cut_off': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'discounts': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'distance': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '10'}),
            'entry_form': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'lodging': ('django.db.models.fields.URLField', [], {'default': "'http://'", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'map_link': ('django.db.models.fields.URLField', [], {'default': "'http://'", 'max_length': '200'}),
            'packet_pickup': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'race_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'reg_description': ('django.db.models.fields.TextField', [], {}),
            'reg_url': ('django.db.models.fields.URLField', [], {'default': "'http://'", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'slogan': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'start_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'unit': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'races.racer': {
            'Meta': {'object_name': 'Racer'},
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['races.EmergencyContact']", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'gender': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'shirt_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'trailhawk': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['members.Member']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        'races.registration': {
            'Meta': {'object_name': 'Registration'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['races.Race']"}),
            'reg_cost': ('django.db.models.fields.IntegerField', [], {}),
            'reg_date': ('django.db.models.fields.DateField', [], {})
        },
        'races.report': {
            'Meta': {'object_name': 'Report'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['races.Race']"}),
            'racer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['races.Racer']"}),
            'report': ('django.db.models.fields.URLField', [], {'default': "'http://'", 'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'races.result': {
            'Meta': {'object_name': 'Result'},
            'bib_number': ('django.db.models.fields.IntegerField', [], {}),
            'course_record': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'dq': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['races.Race']"}),
            'racer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['races.Racer']"}),
            'time': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['races']