# Generated by Django 3.0.4 on 2020-03-28 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='address',
            new_name='district',
        ),
    ]
