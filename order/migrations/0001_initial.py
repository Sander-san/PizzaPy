# Generated by Django 4.1.5 on 2023-01-26 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('food', models.ManyToManyField(blank=True, null=True, related_name='orders', to='menu.foodobject')),
            ],
        ),
    ]
