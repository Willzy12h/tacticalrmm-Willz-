# Generated by Django 4.0.5 on 2022-06-29 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0011_alter_alert_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='action_retcode',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='alert',
            name='resolved_action_retcode',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
