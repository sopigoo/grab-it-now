from django.test import TestCase, Client
from django.urls import reverse
from .models import Product

class mainTest(TestCase):
    def setUp(self):
        # Create a product
        self.product = Product.objects.create(
            name='Test Product',
            price=10000,
            description='This is a test product',
            stock=10,
            category='Test Category',
            rating=4.5
        )

    def test_add_product_view(self):
        # Posting valid data to the add product view
        Client().post(reverse('main:add_product'), {
            'name': 'New Product',
            'price': 2000,
            'description': 'New product description',
            'stock': 5,
            'category': 'New Category',
            'rating': 4.0
        })
        # Ensure that the new product is added to the database
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(Product.objects.last().name, 'New Product')

    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')