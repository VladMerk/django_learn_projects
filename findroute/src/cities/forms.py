from django import forms

from cities.models import Cities


class CitiesForm(forms.ModelForm):
    name = forms.CharField(label='Город',
    error_messages={
            "unique": "Такой город уже существует в базе данных"
        },
    widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите название города',
    }))

    class Meta:
        model = Cities
        fields = ('name', )
