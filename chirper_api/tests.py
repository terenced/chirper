from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token

from chirper_api.serializers import UserCreateSerializer


class ApiTestCase(APITestCase):

    def setUp(self):
        token = Token.objects.get(user__username='horse')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_should_fail_to_get_chirps_without_token(self):
        """
        Ensure we cannot get chirps unless we are authenticated
        """
        unauth_client = APIClient()
        url = reverse('chirp-list')
        response = unauth_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_should_chirps_with_token(self):
        """
        Ensure we can get chirps
        """
        url = reverse('chirp-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        """
        Ensure we can create a new user
        """
        data = {'username': u'jake','password': u'dev123'}

        url = reverse('user-register')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
