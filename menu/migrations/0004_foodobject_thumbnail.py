# Generated by Django 4.1.5 on 2023-01-25 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_foodobject_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodobject',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='static/thumbnail/'),
        ),
    ]
