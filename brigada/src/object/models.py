from django.db import models


class Object(models.Model):
    city = models.ForeignKey('cities.City', on_delete=models.CASCADE, verbose_name='Город')
    team = models.ForeignKey('teams.Team', on_delete=models.CASCADE, verbose_name='Бригада')
    name = models.CharField(max_length=100, verbose_name='Объект')
    amount_people = models.IntegerField(verbose_name='Количество людей')
    head = models.CharField(max_length=200, verbose_name='ФИО ответственного')
    qualification = models.CharField(max_length=150, verbose_name='Должность ответственного')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'
        ordering = ['city', 'team', 'name']
