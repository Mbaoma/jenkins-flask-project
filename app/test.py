import unittest
from main import app


class TestHello(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    # testing our routes
    def test_hello(self):
        response = self.app.get('/')
        self.assertEqual(response.status, '200 OK')


if __name__ == '__main__':
    unittest.main()
