# Generated by Django 2.0.2 on 2018-10-01 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='name',
        ),
        migrations.AddField(
            model_name='location',
            name='location_name',
            field=models.CharField(default=None, max_length=30, unique=True),
            preserve_default=False,
        ),
    ]
