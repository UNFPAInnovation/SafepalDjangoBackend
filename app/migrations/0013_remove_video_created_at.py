# Generated by Django 3.0.4 on 2020-12-02 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_faqrating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='created_at',
        ),
    ]