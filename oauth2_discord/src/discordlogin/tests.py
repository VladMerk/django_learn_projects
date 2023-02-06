from django.test import Client, TestCase
from django.urls import reverse


class DiscordLoginTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_testcase(self):
        response = self.client.get(reverse("oauth2"))
        self.assertEqual(response.status_code, 200)
