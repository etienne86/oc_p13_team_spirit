# Generated by Django 3.0.7 on 2020-09-21 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preorders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppingcart',
            old_name='open',
            new_name='is_open',
        ),
    ]