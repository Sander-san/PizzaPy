# Generated by Django 4.1.5 on 2023-01-27 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_remove_basket_expired'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdelivery',
            name='expired',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ordertakeaway',
            name='expired',
            field=models.BooleanField(default=False),
        ),
    ]
