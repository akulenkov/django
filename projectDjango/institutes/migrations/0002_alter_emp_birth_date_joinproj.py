# Generated by Django 4.0 on 2021-12-10 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institutes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='birth_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата рождения'),
        ),
        migrations.CreateModel(
            name='JoinProj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='institutes.emp', verbose_name='Сотрудник')),
                ('proj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='institutes.projects', verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Участие в проектах',
                'verbose_name_plural': 'Участия в проектах',
                'ordering': ['proj'],
            },
        ),
    ]