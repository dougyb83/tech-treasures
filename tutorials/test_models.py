from django.test import TestCase
from .models import Tutorials
from django.core.exceptions import ValidationError


class TestModels(TestCase):

    def test_create_tutorial(self):
        tutorial = Tutorials.objects.create(
            title='tutorial title',
            description='a tutorial description',
            youtube_url='https://www.youtube.com/',
            youtube_embed_url='https://www.youtube.com/embed/',
            additional_link='link to resource'
        )
        self.assertEqual(tutorial.title, 'tutorial title')
        self.assertEqual(tutorial.description, 'a tutorial description')
        self.assertEqual(tutorial.youtube_url, 'https://www.youtube.com/')
        self.assertEqual
        (tutorial.youtube_embed_url, 'https://www.youtube.com/embed/')
        self.assertEqual(tutorial.additional_link, 'link to resource')

    def test_str_representation(self):
        # Test string representation of the Contact object
        tutorial = Tutorials.objects.create(
            title='tutorial title',
            description='a tutorial description',
            youtube_url='https://www.youtube.com/',
            youtube_embed_url='https://www.youtube.com/embed/',
            additional_link='link to resource'
        )
        self.assertEqual(str(tutorial), 'tutorial title')

    def test_blank_fields(self):
        # Test blank fields validation
        tutorial = Tutorials(title='', description='', youtube_url='')
        with self.assertRaises(ValidationError):
            tutorial.full_clean()

    def test_null_fields(self):
        # Test null fields validation
        tutorial = Tutorials(title=None, description=None, youtube_url=None)
        with self.assertRaises(ValidationError):
            tutorial.full_clean()
