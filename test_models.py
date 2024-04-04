# tests/test_models.py
import unittest
from models import Product
from factories import ProductFactory

class TestProductModel(unittest.TestCase):

    def test_create_product(self):
        product = ProductFactory.create()
        self.assertIsNotNone(product.id)

    def test_find_product_by_name(self):
        name = "Test Product"
        product = ProductFactory.create(name=name)
        # Assume find_by_name is a method to be implemented
        found = Product.find_by_name(name)
        self.assertEqual(found.id, product.id)
