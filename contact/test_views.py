from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Contact


class TestViews(TestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            username='admin', password='adminpassword')

    def test_get_contact(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_get_admin_contact_page(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('admin-contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/admin-contact.html')

    def test_get_admin_contact_reply(self):
        email = Contact.objects.create(
            id=1,
            full_name='Test Test',
            email='test@Test.com',
            message='Test message'
        )
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(
            reverse('admin-contact-reply', kwargs={'email_id': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/admin-contact-reply.html')

    def test_can_reply_email(self):
        email = Contact.objects.create(
            id=1,
            full_name='Test Test',
            email='test@Test.com',
            message='Test message'
        )
        self.client.login(username='admin', password='adminpassword')
        response = self.client.post(
            reverse('reply-email', kwargs={'email_id': 1}), {'reply': 'Test reply'})
        self.assertEqual(response.status_code, 302)

        email.refresh_from_db()
        self.assertTrue(email.have_replied)

    def test_can_delete_email(self):
        email = Contact.objects.create(
            id=1,
            full_name='Test Test',
            email='test@Test.com',
            message='Test message'
        )
        self.client.login(username='admin', password='adminpassword')
        response = self.client.post(
            reverse('delete-email', kwargs={'email_id': 1}))
        self.assertEqual(response.status_code, 302)

        with self.assertRaises(Contact.DoesNotExist):
            email.refresh_from_db()
