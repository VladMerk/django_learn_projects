from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from teams.forms import TeamsForm

from teams.models import Team


class TeamsListView(ListView):
    queryset = Team.objects.all().select_related()
    template_name = 'teams/index.html'


class TeamCreateView(CreateView):
    model = Team
    form_class = TeamsForm
    template_name = 'teams/create.html'
    success_url = reverse_lazy('teams:index')


class TeamUpdateView(UpdateView):
    model = Team
    form_class = TeamsForm
    template_name = 'teams/update.html'
    success_url = reverse_lazy('teams:index')


class TeamDeleteView(DeleteView):
    model = Team
    success_url = reverse_lazy('teams:index')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
