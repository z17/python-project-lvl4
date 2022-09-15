from django.test import Client, TestCase
from django.urls import reverse_lazy

from task_manager.labels.models import Label
from task_manager.users.models import User


class UserTestCase(TestCase):
    fixtures = ['labels.json']

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username="test54")
        self.client.force_login(self.user)
        self.label1 = Label.objects.get(id=1)

    def test_create_label(self):
        url = reverse_lazy('labels:create')

        new_label = {
            'name': 'test_label',
        }

        response = self.client.post(url, new_label, follow=True)
        self.assertRedirects(response, '/labels/')
        Label.objects.get(name=new_label['name'])

    def test_update_label(self):
        url = reverse_lazy('labels:update', args=(self.label1.pk,))
        new_label_name = {
            'name': 'test_label 36435',
        }
        response = self.client.post(url, new_label_name, follow=True)
        self.assertRedirects(response, '/labels/')
        updated_label = Label.objects.get(pk=self.label1.pk)
        self.assertEqual(updated_label.name, new_label_name['name'])

    def test_delete_label(self):
        url = reverse_lazy('labels:delete', args=(self.label1.id,))
        self.client.post(url, follow=True)

        with self.assertRaises(Exception):
            Label.objects.get(pk=self.label1.pk)
