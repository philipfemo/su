from django.test import TestCase
from django.test.client import Client
from .models import User
from django.core.urlresolvers import reverse

# Create your tests here.

class UserTest(TestCase):
    """User model test."""
    def test_str(self):
        user = User(first_name='John', last_name='Doe')
        self.assertEqual(str(user), 'John Doe',)

class UserListViewTests(TestCase):
    """Contact list view test"""
    def test_users_in_the_context(self):
        client = Client()
        response = client.get(reverse('users:user_list'))

        self.assertEqual(list(response.context['object_list']), [])
        User.objects.create(first_name='foo', last_name='bar')
        response = client.get(reverse('users:user_list'))
        self.assertEquals(response.context['object_list'].count(), 1)
