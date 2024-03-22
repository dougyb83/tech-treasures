from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Tutorials


class TestViews(TestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            username='admin', password='adminpassword')
        self.tutorial = Tutorials.objects.create(
            title='tutorial title',
            description='a tutorial description',
            youtube_url='https://youtu.be/2hBOUW3bFQ8?si=CSWRaou9LKC_cRUi',
            youtube_embed_url='https://www.youtube.com/embed/',
            additional_link='link to resource'
        )

    def test_view_tutorials(self):
        response = self.client.get(reverse('view_tutorials'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tutorials/tutorials.html')

    def test_add_tutorial(self):
        self.client.login(username='admin', password='adminpassword')
        new_tutorial = {
            'title': 'New Tutorial',
            'description': 'New Description',
            'youtube_url': 'https://youtu.be/2hBOUW3bFQ8?si=CSWRaou9LKC_cRUi'
            }
        response = self.client.post(reverse('add_tutorial'), new_tutorial)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Tutorials.objects.filter(title='New Tutorial').exists())

    def test_edit_tutorial(self):
        self.client.login(username='admin', password='adminpassword')
        edited_tutorial = {
            'title': 'Updated Tutorial',
            'description': 'Updated Description',
            'youtube_url': 'https://youtu.be/2hBOUW3bFQ8?si=CSWRaou9LKC_cRUi'
            }
        response = self.client.post(
            reverse('edit_tutorial', args=[self.tutorial.id]), edited_tutorial)
        self.assertEqual(response.status_code, 302)
        self.tutorial.refresh_from_db()
        self.assertEqual(self.tutorial.title, 'Updated Tutorial')

    def test_delete_tutorial(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.post(reverse(
            'delete_tutorial', args=[self.tutorial.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Tutorials.objects.filter(title='Test Tutorial').exists())
