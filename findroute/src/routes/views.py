from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView
from cities.models import Cities

from routes.forms import RouteForm, RouteModelForm
from routes.models import Route
from routes.utils import get_routes
from trains.models import Trains

def index(request):
    form = RouteForm()
    return render(request, 'routes/index.html', {'form': form})


def find_routes(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            try:
                context = get_routes(request, form)
            except ValueError as e:
                messages.error(request, e)
                return render(request, 'routes/index.html', {'form': form})
            return render(request, 'routes/index.html', context)
    else:
        form = RouteForm()
        messages.error(request, "Нет данных для отображения")

    return render(request, 'routes/index.html', {'form': form})


def add_route(request):  # sourcery skip: extract-method, use-named-expression
    if request.method == "POST":
        context = {}
        data = request.POST
        if data:
            total_time = int(data['total_time'])
            from_city_id = int(data['from_city'])
            to_city_id = int(data['to_city'])
            trains = data['trains'].split(',')
            trains_lst = [int(t) for t in trains if t.isdigit()]
            qs = Trains.objects.filter(id__in=trains_lst).select_related(
                'from_city', 'to_city')
            cities = Cities.objects.filter(
                id__in=[from_city_id, to_city_id]).in_bulk()
            form = RouteModelForm(
                initial={
                    'from_city': cities[from_city_id],
                    'to_city': cities[to_city_id],
                    'travel_times': total_time,
                    'trains': qs
                         }
            )
            context['form'] = form
        return render(request, 'routes/create.html', context)
    else:
        messages.error(request, "Невозможно сохранить несуществующий маршрут")
        return redirect('/')

def save_route(request):
    if request.method == "POST":
        form = RouteModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Маршрут успешно сохранен")
            return redirect('/')
        return render(request, 'routes/create.html', {'form': form})
    else:
        messages.error(request, "Невозможно сохранить несуществующий маршрут")
        return redirect('/')

class RouteListView(ListView):
    paginate_by = 10
    model = Route
    template_name = 'routes/list.html'


class RouteDetailView(DetailView):
    queryset = Route.objects.all()
    template_name = 'routes/detail.html'


class RouteDeleteView(LoginRequiredMixin, DeleteView):
    model = Route
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Маршрут успешно удален')
        return self.delete(request, *args, **kwargs)
