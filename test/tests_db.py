import unittest
from app import create_app


class DbOperationsTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def tearDown(self):
        # Clean up after the test
        pass

    def test_api(self):
        url = "/operation"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response = response.json
        self.assertEqual(response['success'], True)
        self.assertEqual(1, response['requestId'])
