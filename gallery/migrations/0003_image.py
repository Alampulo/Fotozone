# Generated by Django 2.0.2 on 2018-10-01 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=30)),
                ('image_description', models.TextField()),
                ('image_path', models.ImageField(upload_to='gallery/')),
                ('image_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Category')),
                ('image_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Location')),
            ],
        ),
    ]
