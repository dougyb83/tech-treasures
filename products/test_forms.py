from django.test import TestCase
from .forms import ProductForm
from .models import Category, Product


class ProductFormTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category', slug='test-category')

    def test_product_form_valid_data(self):
        form_data = {
            'name': 'Test Product',
            'description': 'Test Description',
            'category': self.category.id,  # Assuming category ID
            'image': '',  # Assuming image is optional
        }
        form = ProductForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_product_form_invalid_data(self):
        # Test with missing required fields
        form_data = {}
        form = ProductForm(data=form_data)
        self.assertFalse(form.is_valid())

        # Test with invalid category
        form_data = {
            'name': 'Test Product',
            'description': 'Test Description',
            'category': 999,  # Assuming an invalid category ID
            'image': '',  # Assuming image is optional
        }
        form = ProductForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_product_form_widget_attrs(self):
        form = ProductForm()
        self.assertIn('class="border-black rounded-0"', str(form))
