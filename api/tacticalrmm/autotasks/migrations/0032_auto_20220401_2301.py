# Generated by Django 3.2.12 on 2022-04-01 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autotasks', '0031_auto_20220401_2249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='automatedtask',
            name='execution_time',
        ),
        migrations.RemoveField(
            model_name='automatedtask',
            name='last_run',
        ),
        migrations.RemoveField(
            model_name='automatedtask',
            name='parent_task',
        ),
        migrations.RemoveField(
            model_name='automatedtask',
            name='retcode',
        ),
        migrations.RemoveField(
            model_name='automatedtask',
            name='status',
        ),
        migrations.RemoveField(
            model_name='automatedtask',
            name='stderr',
        ),
        migrations.RemoveField(
            model_name='automatedtask',
            name='stdout',
        ),
        migrations.RemoveField(
            model_name='automatedtask',
            name='sync_status',
        ),
    ]
