# Generated by Django 3.0.6 on 2020-05-10 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeetasks',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='employeetasks',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Task Name'),
        ),
        migrations.AlterField(
            model_name='employeetasks',
            name='status',
            field=models.CharField(choices=[('0', 'New'), ('1', 'In Progress'), ('2', 'Completed')], max_length=1, verbose_name='Task Status'),
        ),
    ]
