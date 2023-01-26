# from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from trains.models import Trains
from trains.forms import TrainsForm


class TrainsListView(SuccessMessageMixin, ListView):
    paginate_by = 5
    queryset = Trains.objects.all()
    template_name = 'trains/index.html'
    succes_url = reverse_lazy('trains:index')
    success_message = 'Город успешно добавлен'


class TrainsDetailView(DetailView):
    queryset = Trains.objects.all()
    template_name = 'trains/detail.html'


class TrainsCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Trains
    form_class = TrainsForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('trains:index')
    success_message = 'Поезд успешно добавлен'


class TrainsUpdateView(SuccessMessageMixin, UpdateView):
    model = Trains
    form_class = TrainsForm
    template_name = 'trains/update.html'
    success_url =  reverse_lazy('trains:index')
    success_message = 'Поезд успешно отредактирован'


class TrainsDeleteView(LoginRequiredMixin, DeleteView):
    model = Trains
    template_name = 'trains/delete.html'
    success_url = reverse_lazy('trains:index')

    # Add support for browsers which only accept GET and POST for now.
    def get(self, request, *args, **kwargs):
        messages.success(request, "Поезд успешно удален")
        return self.delete(request, *args, **kwargs)
