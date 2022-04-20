from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Prod(models.Model):
    prod_name = models.CharField('Наименование товара', max_length=50)
    prod_price = models.IntegerField('Цена за 1м²')
    prod_task = models.TextField('Описание товара')

    def __str__(self):
        return self.prod_name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'