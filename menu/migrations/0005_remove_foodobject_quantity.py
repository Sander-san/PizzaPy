# Generated by Django 4.1.5 on 2023-01-27 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_foodobject_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodobject',
            name='quantity',
        ),
    ]
