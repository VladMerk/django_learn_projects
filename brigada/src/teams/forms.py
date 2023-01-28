from django import forms
from cities.models import City

from teams.models import Team


class TeamsForm(forms.ModelForm):
    city = forms.ModelChoiceField(label="Город", queryset=City.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Team
        # fields = ('city', 'name', 'amount_people', 'head', 'qualification')
        fields = '__all__'
