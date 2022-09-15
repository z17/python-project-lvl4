from django.test import Client, TestCase
from django.urls import reverse_lazy

from task_manager.statuses.models import Status
from task_manager.users.models import User


class UserTestCase(TestCase):
    fixtures = ['statuses.json']

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username="test user for statuses")
        self.client.force_login(self.user)
        self.status = Status.objects.get(id=1)

    def test_create_label(self):
        url = reverse_lazy('statuses:create')
        new_status = {
            'name': 'test status creation',
        }
        response = self.client.post(url, new_status, follow=True)
        self.assertRedirects(response, '/statuses/')
        Status.objects.get(name=new_status['name'])

    def test_update_label(self):
        url = reverse_lazy('statuses:update', args=(self.status.pk,))
        new_status_name = {
            'name': 'test status',
        }
        response = self.client.post(url, new_status_name, follow=True)
        self.assertRedirects(response, '/statuses/')
        updated_label = Status.objects.get(pk=self.status.pk)
        self.assertEqual(updated_label.name, new_status_name['name'])

    def test_delete_label(self):
        url = reverse_lazy('statuses:delete', args=(self.status.pk,))
        self.client.post(url, follow=True)

        with self.assertRaises(Exception):
            Status.objects.get(pk=self.status.pk)
