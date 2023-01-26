from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, authenticate
from django.test import TestCase, Client
from django.http import HttpRequest
from django.urls import reverse

from accounts.forms import UserLoginForm, UserRegistrationForm
# Create your tests here.

class AccountsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        user_A = User.objects.create(username='userA')
        user_A.set_password('userA')
        user_A.save()

        user_B = User.objects.create(username='userB')
        user_B.set_password('userB')
        user_B.is_active = False
        user_B.save()

# -----------Test UserLoginForm------------------
    def test_userloginform_accept_user(self):
        '''User is valid'''
        data = {
            'username': 'userA',
            'password': 'userA'
        }

        form = UserLoginForm(data=data)
        self.assertTrue(form.is_valid())

    def test_userloginform_no_user(self):  # sourcery skip: class-extract-method
        '''Username is invalid message'''
        data = {
            'username': 'userC',
            'password': 'userC'
        }

        form = UserLoginForm(data=data)
        self.assertFalse(form.is_valid())

        with self.assertRaisesMessage(ValidationError, 'Такого пользователя нет'):
            form.clean()


    def test_userloginform_wrong_password(self):
        '''Username is invalid message password'''
        data = {
            'username': 'userA',
            'password': 'userC'
        }

        form = UserLoginForm(data=data)
        self.assertFalse(form.is_valid())

        with self.assertRaisesMessage(ValidationError, 'Неверный пароль'):
            form.clean()

    def test_userloginform_user_is_not_active(self):
        '''Username is invalid message - user is not active'''
        data = {
            'username': 'userB',
            'password': 'userB'
        }

        form = UserLoginForm(data=data)
        self.assertFalse(form.is_valid())

        with self.assertRaisesMessage(ValidationError, 'Данный пользователь не активен'):
            form.clean()

# -----------Test UserLoginForm------------------

    def test_userregistrationform_check_password(self):
        data ={
            'username': 'userD',
            'password': 'userD',
            'password2': 'user'
        }
        form = UserRegistrationForm(data=data)
        self.assertFalse(form.is_valid())

        with self.assertRaisesMessage(ValidationError, 'Пароли не совпадают'):
            form.clean_password2()

        data ={
            'username': 'userD',
            'password': 'userD',
            'password2': 'userD'
        }
        form = UserRegistrationForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.clean_password2(), data['password2'])

# -----------Test LoginView----------------------
    def test_loginview_accept(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed('accounts/login.html')

        data = {
            'username': 'userA',
            'password': 'userA'
        }
        response = self.client.post(reverse('accounts:login'), data=data)
        self.assertTrue(response.status_code, 200)

        response = self.client.login(**data)
        # response = self.client.get(reverse('index'))
        self.assertTrue(response)

    def test_logoutview(self):
        # user = authenticate(username='userA', password='userA')
        data = {
            'username': 'userA',
            'password': 'userA'
        }

        response = self.client.post(reverse('accounts:logout'), data)
        self.assertTrue(response.status_code, 200)

    def test_registration_view(self):
        data = {
            'username': 'userD',
            'password': 'userD',
            'password2': 'userD'
        }

        response = self.client.get(reverse('accounts:registration'))
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed('accounts/register.html')

        response = self.client.post(reverse('accounts:registration'), data=data)
        self.assertTrue(response)
