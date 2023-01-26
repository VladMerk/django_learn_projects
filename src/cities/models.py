from django.db import models


class Cities(models.Model):
    name = models.CharField(
        max_length=150, unique=True,
        verbose_name="Город",
        error_messages={'unique': 'Такой город уже существует в базе данных'})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['name']
