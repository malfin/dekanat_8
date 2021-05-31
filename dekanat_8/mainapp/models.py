from django.db import models


class Group(models.Model):
    name = models.CharField(verbose_name='название группы', max_length=256)
