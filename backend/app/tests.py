import unittest
from settings.config import Config
from main import create_app


class TestCase(unittest.TestCase):
    def setUp(self):
        Config.TESTING = True
        self.app = create_app(name='SANIC')

    def tearDown(self):
        pass

    def test_route(self):
        response = self.app.get(f'http://127.0.0.1:8000/')
        self.assertEquals(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
