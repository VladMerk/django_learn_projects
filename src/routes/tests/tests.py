from django.test import TestCase
from django.urls import reverse

import routes
from routes.forms import RouteForm
from routes.utils import dfs_paths, get_graph
from cities.models import Cities
from trains.models import Trains


class RoutesTestCase(TestCase):
    def setUp(self):
       self.city_A = Cities.objects.create(name='A')
       self.city_B = Cities.objects.create(name='B')
       self.city_C = Cities.objects.create(name='C')
       self.city_D = Cities.objects.create(name='D')
       self.city_E = Cities.objects.create(name='E')

       lst = [
        Trains(name='t1', from_city=self.city_A, to_city=self.city_B,
        travel_time=9),
        Trains(name='t2', from_city=self.city_B, to_city=self.city_A,
        travel_time=11),
        Trains(name='t3', from_city=self.city_B, to_city=self.city_C,
        travel_time=12),
        Trains(name='t4', from_city=self.city_C, to_city=self.city_B,
        travel_time=8),
        Trains(name='t5', from_city=self.city_B, to_city=self.city_D,
        travel_time=17),
        Trains(name='t6', from_city=self.city_D, to_city=self.city_B,
        travel_time=21),
        Trains(name='t7', from_city=self.city_B, to_city=self.city_E,
        travel_time=23),
        Trains(name='t8', from_city=self.city_E, to_city=self.city_B,
        travel_time=19),
        Trains(name='t9', from_city=self.city_D, to_city=self.city_E,
        travel_time=9),
       ]
       Trains.objects.bulk_create(lst)

    def test_home_routes_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'routes/index.html')
        self.assertEqual(response.resolver_match.func, routes.views.index)

    def test_find_all_routes(self):
        qs = Trains.objects.all()
        graph = get_graph(qs)
        all_routes = list(dfs_paths(graph, self.city_A.id, self.city_E.id))
        self.assertEqual(len(all_routes), 2)

    def test_valid_route_form(self):
        data = {'from_city': self.city_A.id, 'to_city': self.city_B.id,
                'cities': [self.city_E.id, self.city_D.id],
                'travelling_time': 9
                }
        form = RouteForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_route_form(self):
        data = {'from_city': self.city_A.id, 'to_city': self.city_B.id,
                'cities': [self.city_E.id, self.city_D.id],
                }
        form = RouteForm(data=data)
        self.assertFalse(form.is_valid())
