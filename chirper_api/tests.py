from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token

from chirper_api.serializers import UserRegistrationSerializer
import json


class ApiTestCase(APITestCase):

    def __init__(self, *args, **kwargs):
        super(ApiTestCase, self).__init__(*args, **kwargs)
        self.unauth_client = None

    def setUp(self):
        token = Token.objects.get(user__username='horse')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        self.unauth_client = APIClient(enforce_csrf_checks=True)

    def test_should_fail_to_get_chirps_without_token(self):
        """
        Ensure we cannot get chirps unless we are authenticated
        """
        url = reverse('chirp-list')
        response = self.unauth_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_should_chirps_with_token(self):
        """
        Ensure we can get chirps
        """
        url = reverse('chirp-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_regisiter_user(self):
        """
        Ensure we can create a new user
        """
        data = {'username': u'jake','password': u'dev123'}

        url = reverse('register-user')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_should_register_user_with_unauth_client(self):
        """
        Ensure we can create a new user with an unauthenicated client
        """
        url = reverse('register-user')
        data = {'username': u'registerme','password': u'somepassword', 'first_name': u'first', 'last_name': u'last'}

        response = self.unauth_client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(username = data['username'])

        assert user is not None
        self.assertEqual(user.username, data['username'])

    def test_should_get_token_with_valid_creds(self):
        expected_token = Token.objects.get(user__username='horse')
        url = reverse('token-auth')
        data = {'username': u'horse','password': u'dev123'}

        response = self.client.post(url, data)
        actual_token = json.loads(response.content)["token"]
        self.assertEqual(actual_token, expected_token.key)

    def test_should_not_get_token_with_invalid_creds(self):
        url = reverse('token-auth')
        data = {'username': u'hacker','password': u'somepassword'}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_should_access_auth_token_with_unauth_client(self):
        expected_token = Token.objects.get(user__username='horse')
        url = reverse('token-auth')
        data = {'username': u'horse','password': u'dev123'}

        response = self.unauth_client.post(url, data)
        actual_token = json.loads(response.content)["token"]
        self.assertEqual(actual_token, expected_token.key)

    def test_should_access_auth_token_with_new_user(self):
        user = User(username = 'newuser', password = 'test')
        user.save()

        token = Token.objects.get(user__username = user.username)

        url = reverse('token-auth')
        data = {'username': u'newuser','password': u'test'}

        response = self.unauth_client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        actual_token = json.loads(response.content)["token"]
        self.assertEqual(actual_token, expected_token.key)

    def test_should_create_chirp_belonging_to_authenticated_user(self):
        url = reverse('create-chirp')
        data = {'chirp': 'Hello, world!'}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_new_user_should_see_no_chirps(self):
        user = User(username = 'newuser', password = 'test')
        user.save()
        token = Token.objects.get(user__username='newuser')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        url = reverse('chirp-list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, '[]')

class ModelTestCase(TestCase):
    def test_user_should_have_token_after_created(self):
        user = User(username = 'test', password = 'test')
        user.save()
        token = Token.objects.get(user__username = 'test')
        assert token is not None
        assert token.key is not None
