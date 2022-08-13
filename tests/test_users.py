from django.contrib.auth.models import User
from django.test import TestCase


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="test54")

    def test_user(self):
        user = User.objects.get(username="test54")
        self.assertEqual(user.username, "test54")
