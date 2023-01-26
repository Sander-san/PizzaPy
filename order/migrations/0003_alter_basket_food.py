# Generated by Django 4.1.5 on 2023-01-26 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
        ('order', '0002_remove_basket_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='food',
            field=models.ManyToManyField(blank=True, related_name='orders', to='menu.foodobject'),
        ),
    ]
