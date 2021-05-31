from django.db import models


class Group(models.Model):
    name = models.CharField(verbose_name='название группы', max_length=256)
    desc = models.TextField(verbose_name='Специальность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'группы'


class Student(models.Model):
    group = models.ForeignKey(Group, verbose_name='группа', on_delete=models.CASCADE)
    surname = models.CharField(verbose_name='фамилия', max_length=128)
    name = models.CharField(verbose_name='имя', max_length=128)
    patronymic = models.CharField(verbose_name='отчество', max_length=128, blank=True)

    def __str__(self):
        return f'{self.surname} | {self.group}'

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
