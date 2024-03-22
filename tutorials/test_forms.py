from django.test import TestCase
from .forms import TutorialForm
from .models import Tutorials


class TestForms(TestCase):

    def test_fields_are_explicit_in_form_metaclass(self):
        form = TutorialForm()
        self.assertEqual(form.Meta.model, Tutorials)
        self.assertEqual(form.Meta.fields, [
            'title', 'description', 'youtube_url', 'additional_link'])

    def test_title_is_required(self):
        form = TutorialForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_description_is_required(self):
        form = TutorialForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(
            form.errors['description'][0], 'This field is required.')

    def test_youtube_url_is_required(self):
        form = TutorialForm({'youtube_url': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('youtube_url', form.errors.keys())
        self.assertEqual(
            form.errors['youtube_url'][0], 'This field is required.')

    def test_valid_data(self):
        form = TutorialForm({
            'title': 'tutorial title',
            'description': 'tutorial description',
            'youtube_url': 'youtube url',
            'additional_link': 'additional link'
            })
        self.assertTrue(form.is_valid())
