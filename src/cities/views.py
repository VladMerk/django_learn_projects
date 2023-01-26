# from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from cities.models import Cities
from cities.forms import CitiesForm

class CitiesListView(SuccessMessageMixin, ListView):
    paginate_by = 5
    queryset = Cities.objects.all()
    template_name = 'cities/index.html'
    succes_url = reverse_lazy('cities:index')
    success_message = 'Город успешно добавлен'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CitiesForm()
        return context


class CitiesDetailView(DetailView):
    queryset = Cities.objects.all()
    template_name = 'cities/detail.html'


class CitiesCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Cities
    form_class = CitiesForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:index')
    success_message = 'Город успешно добавлен'


class CitiesUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Cities
    form_class = CitiesForm
    template_name = 'cities/update.html'
    success_url =  reverse_lazy('cities:index')
    success_message = 'Город успешно отредактирован'


class CitiesDeleteView(LoginRequiredMixin, DeleteView):
    model = Cities
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:index')

    # Add support for browsers which only accept GET and POST for now.
    def get(self, request, *args, **kwargs):
        messages.success(request, "Город успешно удален")
        return self.delete(request, *args, **kwargs)
