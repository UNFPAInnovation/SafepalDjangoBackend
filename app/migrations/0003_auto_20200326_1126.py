# Generated by Django 3.0.4 on 2020-03-26 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='duration',
            field=models.IntegerField(default=3),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('content', models.TextField()),
                ('questions', models.TextField()),
                ('thumbnail', models.CharField(max_length=600)),
                ('rating', models.IntegerField(default=5)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Category')),
            ],
        ),
    ]
