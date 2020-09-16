# Generated by Django 3.0.7 on 2020-09-09 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20200908_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='has_private_profile',
            field=models.BooleanField(default=False, help_text='Si cette case est cochée, mes informations ne seront pas visibles par les autres adhérents.', verbose_name='Profil privé ?'),
        ),
    ]