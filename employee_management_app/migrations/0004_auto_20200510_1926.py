# Generated by Django 3.0.6 on 2020-05-10 19:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management_app', '0003_auto_20200510_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeetasks',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 10, 19, 26, 1, 998279)),
        ),
        migrations.AlterField(
            model_name='employeetasks',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 10, 19, 26, 1, 998315)),
        ),
    ]
