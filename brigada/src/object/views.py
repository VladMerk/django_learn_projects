import json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from object.forms import ObjectForm
from object.models import Object
from teams.models import Team


class ObjectListView(ListView):
    queryset = Object.objects.all().select_related()
    template_name = 'object/index.html'


class ObjectCreateView(CreateView):
    model = Object
    form_class = ObjectForm
    template_name = 'object/create.html'
    success_url = reverse_lazy('object:index')


class ObjectDeleteView(DeleteView):
    model = Object
    success_url = reverse_lazy('object:index')

    def get(self, request, *args, **kwargs):
        return self.delete(request)

def get_team(request, city_id):  # sourcery skip: instance-method-first-arg-name
    teams = Team.objects.filter(city__id=city_id)
    print(list(teams.values('id', 'name')))
    return JsonResponse(list(teams.values('id', 'name')), safe=False)

def get_object(request, team_id):
    team_object = get_object_or_404(Team, pk=team_id)
    print(team_object.id, team_object.name, team_object.amount_people)
    data = json.dumps({
        'id': team_object.id,
        'name': team_object.name,
        'amount_people': team_object.amount_people,
        'head': team_object.head,
        'qualification': team_object.qualification
    })
    return JsonResponse(data, safe=False)
