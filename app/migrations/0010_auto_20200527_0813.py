# Generated by Django 3.0.4 on 2020-05-27 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20200520_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.FileField(help_text='Get low res version of video by replacing xyz.mp4 with xyz_480p.m38u', upload_to='videos/'),
        ),
    ]
