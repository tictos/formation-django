# Generated by Django 4.0.4 on 2022-12-24 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voir', '0003_alter_task_scheldule_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='scheldule_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 31, 14, 20, 56, 129980)),
        ),
    ]
