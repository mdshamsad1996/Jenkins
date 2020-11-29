import unittest
from src.app import app

class TestHello(unittest.TestCase):
    """Unitetest for an hello api"""

    def setUp(self):

        """set up method"""
        self.app = app.test_client()

    def test_hello(self):
        actual = self.app.get('/')

        self.assertEqual(actual.status, '200 OK')

        self.assertEqual(actual.data, b'Hello World!')

if __name__ == '__main__':
    unittest.main()