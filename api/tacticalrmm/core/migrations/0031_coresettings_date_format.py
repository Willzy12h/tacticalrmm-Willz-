# Generated by Django 3.2.12 on 2022-03-17 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_coresettings_mesh_device_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='coresettings',
            name='date_format',
            field=models.CharField(blank=True, default='MMM-DD-YYYY - HH:mm', max_length=30),
        ),
    ]
