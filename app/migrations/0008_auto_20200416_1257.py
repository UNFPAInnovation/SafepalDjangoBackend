# Generated by Django 3.0.4 on 2020-04-16 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_quiz_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='article',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Article'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quiz',
            name='thumbnail',
            field=models.CharField(default='https://us.123rf.com/450wm/soifer/soifer1809/soifer180900063/110272407-stock-vector-quiz-time-neon-sign-vector-quiz-pub-design-template-neon-sign-light-banner-neon-signboard-nightly-br.jpg?ver=6', max_length=600),
        ),
    ]
