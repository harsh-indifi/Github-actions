import unittest
from app import create_app
from computation.calculation import Calculation


class AdditionTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def tearDown(self):
        # Clean up after the test
        pass

    def test_api(self):
        url = "/v1/calculation"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_addition(self):
        result = Calculation().add(5, 10)
        self.assertEqual(result, 15)

    def test_addition_2(self):
        result = Calculation().add(5, 10)
        self.assertEqual(result, 15)
