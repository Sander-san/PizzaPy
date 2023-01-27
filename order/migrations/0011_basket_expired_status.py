# Generated by Django 4.1.5 on 2023-01-27 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0010_remove_orderdelivery_restaurant_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='expired',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basket', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='order.basket')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
