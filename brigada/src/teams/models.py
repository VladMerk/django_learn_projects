from django.db import models


class Team(models.Model):
    city = models.ForeignKey('cities.City', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Город')
    name = models.CharField(max_length=100, verbose_name='Бригада')
    amount_people = models.IntegerField(verbose_name='Количество людей')
    head = models.CharField(max_length=200, verbose_name='ФИО ответственного')
    qualification = models.CharField(max_length=150, verbose_name='Должность ответственного')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Бригада"
        verbose_name_plural = "Бригады"
        ordering = ['city', 'name']
