from django.test import TestCase
from .models import Contact
from django.core.exceptions import ValidationError


class TestModels(TestCase):

    def test_create_contact(self):
        # Test creating a contact object
        contact = Contact.objects.create(
            full_name='Test Test',
            email='test@test.com',
            message='Test message'
        )
        self.assertEqual(contact.full_name, 'Test Test')
        self.assertEqual(contact.email, 'test@test.com')
        self.assertEqual(contact.message, 'Test message')
        self.assertFalse(contact.have_read)
        self.assertFalse(contact.have_replied)

    def test_str_representation(self):
        # Test string representation of the Contact object
        contact = Contact.objects.create(
            full_name='Jane Smith',
            email='test@test.com',
            message='test message 2'
        )
        self.assertEqual(str(contact), 'test@test.com')

    def test_blank_fields(self):
        # Test blank fields validation
        contact = Contact(full_name='', email='', message='')
        with self.assertRaises(ValidationError):
            contact.full_clean()

    def test_null_fields(self):
        # Test null fields validation
        contact = Contact(full_name=None, email=None, message=None)
        with self.assertRaises(ValidationError):
            contact.full_clean()

    def test_email_validation(self):
        # Test email field validation
        invalid_email = 'invalid-email'
        contact = Contact(full_name='Test', email=invalid_email, message='')
        with self.assertRaises(ValidationError):
            contact.full_clean()
