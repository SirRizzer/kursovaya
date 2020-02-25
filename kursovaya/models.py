from django.db import models


class Statistic(models.Model):
    subject = models.CharField(db_index=True, blank=False,
                               verbose_name='Студент',
                               null=False,
                               max_length=50, )
    min_mark = models.DecimalField(
        db_index=True,
        blank=False,
        verbose_name='Минимальный балл',
        null=False,
        decimal_places=2,
        max_digits=10,
        default=0, )
    max_mark = models.DecimalField(
        db_index=True,
        blank=False,
        verbose_name='Максимальный балл',
        null=False,
        decimal_places=2,
        max_digits=10,
        default=0,
    )
