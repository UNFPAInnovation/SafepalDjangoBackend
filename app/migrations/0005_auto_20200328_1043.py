# Generated by Django 3.0.4 on 2020-03-28 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200328_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0.3476, max_digits=9),
        ),
        migrations.AlterField(
            model_name='organization',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=32.5825, max_digits=9),
        ),
    ]
