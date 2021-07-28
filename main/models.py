from django.db import models


class CommonInfo(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    rubric = models.ForeignKey('Rubric', null=True,
                                        on_delete=models.PROTECT,
                                        verbose_name='Рубрика')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.title} {self.price}$'


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Haзвaниe')

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'