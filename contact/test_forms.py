from django.test import TestCase
from .forms import ContactForm
from .models import Contact


class TestForms(TestCase):

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ContactForm()
        self.assertEqual(form.Meta.model, Contact)
        self.assertEqual(form.Meta.fields, ['full_name', 'email', 'message'])

    def test_full_name_is_required(self):
        form = ContactForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(form.errors['full_name'][0], 'This field is required.')

    def test_email_is_required(self):
        form = ContactForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_message_is_required(self):
        form = ContactForm({'message': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors.keys())
        self.assertEqual(form.errors['message'][0], 'This field is required.')

    def test_valid_data(self):
        form = ContactForm({
            'full_name': 'Test Test',
            'email': 'test@test.com',
            'message': 'Test message.'
        })
        self.assertTrue(form.is_valid())
