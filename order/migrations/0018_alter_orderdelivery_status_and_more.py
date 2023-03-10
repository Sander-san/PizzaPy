# Generated by Django 4.1.5 on 2023-01-27 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0017_alter_orderdelivery_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdelivery',
            name='status',
            field=models.CharField(auto_created=True, choices=[('1', 'Pending'), ('2', 'In process'), ('3', 'Order complete'), ('4', 'Courier picked up the order'), ('5', 'Courier delivered the order')], default='Pending', max_length=64),
        ),
        migrations.AlterField(
            model_name='ordertakeaway',
            name='status',
            field=models.CharField(auto_created=True, choices=[('1', 'Pending'), ('2', 'In process'), ('3', 'Order complete')], default='Pending', max_length=20),
        ),
    ]
