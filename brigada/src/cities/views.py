from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView

from cities.forms import CityForm
from cities.models import City


class CityListView(ListView):
    model = City
    template_name = 'cities/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CityForm()
        context["form"] = form
        return context


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'


class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:index')


class CityDeleteView(DeleteView):
    model = City
    success_url = reverse_lazy('cities:index')

    def get(self, request, *args, **kwargs):
        return self.delete(request)
