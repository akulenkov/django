# Generated by Django 4.0 on 2021-12-10 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutes', '0002_alter_emp_birth_date_joinproj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='end_date',
            field=models.DateTimeField(verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='start_date',
            field=models.DateTimeField(verbose_name='Дата начала'),
        ),
    ]
