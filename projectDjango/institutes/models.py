from django.db import models


# Create your models here.

class Emp(models.Model):
    last_name = models.CharField(max_length=20, db_index=True, verbose_name='Фамилия')
    first_name = models.CharField(max_length=20,db_index=True,  verbose_name='Имя')
    mid_name = models.CharField(max_length=20, db_index=True, verbose_name='Отчество')
    num_ser_pass = models.IntegerField(db_index=True, verbose_name='Серия и номер паспорта')
    inn = models.IntegerField(db_index=True, verbose_name='ИНН')
    birth_date = models.DateTimeField(auto_now_add = True, verbose_name='Дата рождения')
    position = models.CharField(max_length=50, db_index=True, verbose_name='Должность')

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудник'
        ordering = ['last_name']


class Projects(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    start_date = models.DateTimeField(verbose_name='Дата начала')
    end_date = models.DateTimeField(verbose_name='Дата окончания')
    volume = models.FloatField(verbose_name='Объем финансирования')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Проекты'
        verbose_name = 'Проект'
        ordering = ['name']


class JoinProj(models.Model):
    proj = models.ForeignKey('Projects', null=True, on_delete=models.PROTECT, verbose_name='Проект')
    emp = models.ForeignKey('Emp', null=True, on_delete=models.PROTECT, verbose_name='Сотрудник')

 #   def __str__(self):
   #     return self.proj

    class Meta:
        verbose_name_plural = 'Участия в проектах'
        verbose_name = 'Участие в проектах'
        ordering = ['proj']

