# Generated by Django 4.1.5 on 2023-01-27 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0023_alter_orderdelivery_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, default='1', null=True),
        ),
    ]
