from django.test import Client, TestCase
from django.urls import reverse_lazy

from task_manager.users.models import User


class UserTestCase(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.get(pk=1)

    def test_create_user(self):
        url = reverse_lazy('users:create')

        new_user = {
            'first_name': 'test',
            'last_name': 'test',
            'username': 'test',
            'password1': 'asdnlk@klnsdf',
            'password2': 'asdnlk@klnsdf',
        }

        response = self.client.post(url, new_user, follow=True)
        self.assertRedirects(response, '/login/')

    def test_update_user(self):
        self.client.force_login(self.user1)
        url = reverse_lazy('users:update', args=(self.user1.id,))
        update_user_data = {
            'username': self.user1.username,
            'first_name': self.user1.first_name,
            'last_name': 'new last name',
            'password1': self.user1.password,
            'password2': self.user1.password,
        }
        self.client.post(url, update_user_data, follow=True)

        updated_user = User.objects.get(id=self.user1.id)

        self.assertEqual(updated_user.last_name, update_user_data['last_name'])

    def test_delete_user(self):
        user = self.user1
        self.client.force_login(user)
        url = reverse_lazy('users:delete', args=(user.id,))
        self.client.post(url, follow=True)

        with self.assertRaises(Exception):
            User.objects.get(pk=self.user1.pk)
