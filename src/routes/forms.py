from django import forms

from cities.models import Cities
from routes.models import Route
from trains.models import Trains


class RouteForm(forms.Form):
    from_city = forms.ModelChoiceField(queryset=Cities.objects.all(),
                                    widget=forms.Select(attrs={
                                        'class': 'form-control js-example-basic-single',
                                    }))
    to_city = forms.ModelChoiceField(queryset=Cities.objects.all(),
                                    widget=forms.Select(attrs={
                                        'class': 'form-control js-example-basic-single',
                                    }))
    cities = forms.ModelMultipleChoiceField(label="Через города", queryset=Cities.objects.all(),
                                                required=False, widget=forms.SelectMultiple(attrs={
                                                    'class': 'form-control js-example-basic-multiple',
                                                }))
    travelling_time = forms.IntegerField(label="Время в пути", widget=forms.NumberInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Время в пути',
                            }))


class RouteModelForm(forms.ModelForm):
    name = forms.CharField(
        label='Название маршрута', widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название маршрута'
    }))
    from_city = forms.ModelChoiceField(
        queryset=Cities.objects.all(), widget=forms.HiddenInput()
    )
    to_city = forms.ModelChoiceField(
        queryset=Cities.objects.all(), widget=forms.HiddenInput()
    )
    trains = forms.ModelMultipleChoiceField(
        queryset=Trains.objects.all(),
        required=False, widget=forms.SelectMultiple(
            attrs={'class': 'form-control d-none'}
        )
    )
    travel_times = forms.IntegerField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Route
        fields = '__all__'
