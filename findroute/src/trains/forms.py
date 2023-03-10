from django import forms

from cities.models import Cities
from trains.models import Trains


class TrainsForm(forms.ModelForm):
    name = forms.CharField(label='Номер поезда',
                            widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Введите номер поезда',
                            }))
    travel_time = forms.IntegerField(label="Время в пути", widget=forms.NumberInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Время в пути',
                            }))
    from_city = forms.ModelChoiceField(label='Откуда', queryset=Cities.objects.all(),
                                    widget=forms.Select(attrs={
                                        'class': 'form-control',
                                    }))
    to_city = forms.ModelChoiceField(label='Куда', queryset=Cities.objects.all(),
                                    widget=forms.Select(attrs={
                                        'class': 'form-control',
                                    }))

    class Meta:
        model = Trains
        fields = '__all__'
