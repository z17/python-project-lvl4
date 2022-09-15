from django.test import Client, TestCase
from django.urls import reverse_lazy

from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User


class UserTestCase(TestCase):
    fixtures = ['tasks.json']

    def setUp(self):
        self.client = Client()
        self.user = User.objects.get(pk=1)
        self.client.force_login(self.user)
        self.status = Status.objects.create(name='some status')
        self.task = Task.objects.get(pk=1)

    def test_create_task(self):
        url = reverse_lazy('tasks:create')
        new = {
            'name': 'some task 657',
            'status': self.status.pk,
            'description': 'some_descr'
        }
        response = self.client.post(url, new, follow=True)
        self.assertRedirects(response, '/tasks/')
        created = Task.objects.get(name=new['name'])
        self.assertEqual(created.description, new['description'])

    def test_update_task(self):
        url = reverse_lazy('tasks:update', args=(self.task.pk,))
        new_task = {
            'name': 'some new nametask',
            'status': self.task.status.id,
            'description': self.task.description
        }
        response = self.client.post(url, new_task, follow=True)
        self.assertRedirects(response, '/tasks/')
        updated_label = Task.objects.get(pk=self.task.pk)
        self.assertEqual(updated_label.name, new_task['name'])

    def test_delete_task(self):
        url = reverse_lazy('tasks:delete', args=(self.task.pk,))
        response = self.client.post(url, follow=True)

        self.assertRedirects(response, '/tasks/')
        with self.assertRaises(Exception):
            a = Task.objects.get(pk=self.task.pk)
