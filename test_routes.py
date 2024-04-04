# tests/test_routes.py
import unittest
from app import app

class TestProductRoutes(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_product(self):
        response = self.app.get('/products/1')
        self.assertEqual(response.status_code, 200)
