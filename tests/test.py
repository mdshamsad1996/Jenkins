import unittest
from src.app import app

class TestHello(unittest.TestCase):
    """Unitetest"""

    def setUp(self):
        """set up method"""
        # app.testing = True
        self.app = app.test_client()

    def test_hello(self):
        actual = self.app.get('/')

        self.assertEqual(actual.status, '200 OK')

        self.assertEqual(actual.data, b'Hello World!')

if __name__ == '__main__':
    unittest.main()