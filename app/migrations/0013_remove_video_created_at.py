<<<<<<< HEAD
# Generated by Django 3.0.4 on 2020-09-19 11:26
=======
# Generated by Django 3.0.4 on 2020-12-02 14:33
>>>>>>> b7be096a80fe652ce12f81fe37ac289b148f17b2

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
