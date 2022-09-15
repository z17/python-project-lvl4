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
        created_label = Label.objects.get(name=new_label['name'])
        self.assertEqual(created_label.name, new_label['name'])

    def test_update_label(self):
        print('')

    def test_delete_label(self):
        print('')
