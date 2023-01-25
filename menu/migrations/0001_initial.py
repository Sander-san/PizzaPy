# Generated by Django 4.1.5 on 2023-01-25 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='FoodObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='food_image/')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('regular_size', models.FloatField()),
                ('big_size', models.FloatField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.foodcategory')),
            ],
        ),
    ]
