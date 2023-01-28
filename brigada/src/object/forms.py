from django import forms
from django.db.models import Count

from object.models import Object
from cities.models import City
from teams.models import Team


class ObjectForm(forms.ModelForm):
    city = forms.ModelChoiceField(
        queryset=City.objects.annotate(team_count=Count('team__id')).filter(team_count__gt=0),
        label='Город',
        empty_label="Выберите город",
        widget=forms.Select(attrs={
        'class': 'form-select',
    }))
    team = forms.ModelChoiceField(
        queryset=Team.objects.all(),
        label='Бригада',
        empty_label="Выберите бригаду",
        widget=forms.Select(attrs={
        'class': 'form-select',
    }))
    name = forms.CharField(label='Имя объекта', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    amount_people = forms.IntegerField(label='Количество людей в бригаде', widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    head = forms.CharField(label='ФИО ответственного', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    qualification = forms.CharField(label='Должность ответственного', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Object
        fields = '__all__'
