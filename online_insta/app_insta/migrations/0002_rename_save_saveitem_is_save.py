# Generated by Django 5.1.7 on 2025-03-22 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_insta', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saveitem',
            old_name='save',
            new_name='is_save',
        ),
    ]
