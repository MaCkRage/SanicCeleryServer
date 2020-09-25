import unittest
from .settings import Config
from .main import create_app


class TestCase(unittest.TestCase):
    def setUp(self):
        Config.TESTING = True
        self.app = create_app().test_client()

    def tearDown(self):
        pass

    def test_health_route(self):
        response = self.app.get(f'http://127.0.0.1:5000/health')
        self.assertEquals(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
