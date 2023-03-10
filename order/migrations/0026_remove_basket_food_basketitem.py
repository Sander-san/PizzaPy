# Generated by Django 4.1.5 on 2023-01-31 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_remove_foodobject_quantity'),
        ('order', '0025_remove_basket_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='food',
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.basket')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.foodobject')),
            ],
        ),
    ]
