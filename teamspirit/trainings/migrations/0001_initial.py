# Generated by Django 3.0.7 on 2020-06-10 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_location'),
        ('profiles', '0003_auto_20200609_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_weekly', models.BooleanField(default='False', verbose_name='Entraînement hebdomadaire')),
                ('date', models.CharField(max_length=10)),
                ('day', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=5)),
                ('content', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=1000)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Location')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Personal')),
            ],
        ),
    ]
