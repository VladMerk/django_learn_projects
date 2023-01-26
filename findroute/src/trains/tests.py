from django.test import TestCase, Client
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.urls import reverse

from trains.models import Trains
from cities.models import Cities


class TrainsTestCase(TestCase):

    def setUp(self):
        self.city_a = Cities.objects.create(name='A')
        self.city_b = Cities.objects.create(name='B')

        self.train = Trains.objects.create(
            name = 'tr', travel_time=12,
            from_city = self.city_a, to_city = self.city_b,
        )
        User = get_user_model()
        self.user = User.objects.create_user(
            username = 'User',
            password = 'user'
        )


    def test_train_model_str(self):
        self.assertEqual(str(self.train), 'Поезд №:tr из города A')

    def test_trains_model_clean(self):
        with self.assertRaisesMessage(ValidationError, 'Изменить город прибытия'):
            Trains.objects.create(
                name='tr1', travel_time=14,
                from_city=self.city_a, to_city=self.city_a
            )
        with self.assertRaisesMessage(ValidationError, 'Изменить время в пути'):
            Trains.objects.create(
                name='tr', travel_time=12,
                from_city=self.city_a, to_city=self.city_b
            )

    def test_train_deleteview_messages(self):
        client = Client()
        client.login(username='User', password='user')
        train = Trains.objects.first()
        client.get(reverse('trains:delete', kwargs={'pk': train.pk}))
        response = client.get(reverse('trains:index'))
        messages = list(response.context['messages'])
        self.assertTrue(len(messages))
        self.assertEqual(str(messages[0]), 'Поезд успешно удален')
