# Generated by Django 4.1.5 on 2023-01-25 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_foodcategory_options_alter_foodobject_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodobject',
            name='image',
            field=models.ImageField(upload_to='static/food_img/'),
        ),
    ]