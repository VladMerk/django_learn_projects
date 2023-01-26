from django.test import TestCase, Client
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.contrib.auth import get_user_model

from cities.models import Cities
from cities.forms import CitiesForm


class CitiesTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.city = Cities.objects.create(name='City')
        User = get_user_model()
        cls.user = User.objects.create_user(
            username='User',
            password='user'
        )

    def test_cities_name(self):
        city = Cities.objects.get(name='City')
        self.assertEqual(str(city), 'City')

    def test_cities_form(self):
        city = Cities(name='City')
        with self.assertRaisesMessage(ValidationError, 'Такой город уже существует в базе данных'):
            city.full_clean()

    def test_cities_listview(self):
        response = self.client.get(reverse('cities:index'))
        self.assertTrue(response.status_code, 200)
        self.assertIn('form', response.context)

    def test_cities_deleteview(self):
        client = Client()
        client.login(username='User', password='user')
        city = Cities.objects.first()
        client.get(reverse('cities:delete', kwargs={'pk': city.pk}))
        response = client.get(reverse('cities:index'))
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Город успешно удален")
