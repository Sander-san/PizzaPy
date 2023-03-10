# Generated by Django 4.1.5 on 2023-01-27 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0022_remove_basket_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdelivery',
            name='status',
            field=models.CharField(auto_created=True, choices=[('1', 'Pending'), ('2', 'In process'), ('3', 'Order complete, waiting for courier'), ('4', 'Courier picked up the order'), ('5', 'Courier delivered the order')], default='Pending', max_length=64),
        ),
    ]
