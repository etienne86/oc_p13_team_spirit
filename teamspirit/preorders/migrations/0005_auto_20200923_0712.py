# Generated by Django 3.0.7 on 2020-09-23 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preorders', '0004_auto_20200923_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcartline',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='Quantité'),
        ),
    ]
