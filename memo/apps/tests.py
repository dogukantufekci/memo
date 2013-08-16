from django.contrib.auth.models import User
from django.test import TestCase

from .forms import AppForm
from .models import App


class AppTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='dogukan', email='dogukan@creco.co', password='dogukan')
        
        form = AppForm(initial={'title': 'Memo Admin', 'id_created_by': user.id})
        if form.is_valid():
            form.save()
        form = AppForm(initial={'title': 'Memo Profiles', 'id_created_by': user.id})
        if form.is_valid():
            form.save()
        form = AppForm(initial={'title': 'CRECO Assets', 'id_created_by': user.id})
        if form.is_valid():
            form.save()

    def test_user_can_create_apps(self):
        app_count = App.objects.all().count()
        self.assertEqual(app_count, 3)