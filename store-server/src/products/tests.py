from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from products.models import ProductCategory


class ProductsTestCase(TestCase):

    def setUp(self):
        cities = [
            ProductCategory(name='Cloth'),
            ProductCategory(name='Shoes'),
        ]
        ProductCategory.objects.bulk_create(cities)

    def test_str_productcategory(self):
        city = ProductCategory.objects.get(name='Cloth')
        self.assertEqual(str(city), 'Cloth')

    def test_unique_productcategory(self):
        obj = ProductCategory(name='Cloth')
        with self.assertRaisesMessage(ValidationError, 'Категория продуктов должна быть уникальной'):
            obj.full_clean()

    def test_view_index(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'products/index.html')

    def test_view_products(self):
        response = self.client.get(reverse('products:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('title', response.context)
        self.assertTrue('products', response.context)
        self.assertTrue('categories', response.context)
        self.assertTemplateUsed(response, 'products/products.html')
