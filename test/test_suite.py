import unittest

from test.tests_addition import AdditionTest
from test.tests_db import DbOperationsTest


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTests([
        unittest.TestLoader().loadTestsFromTestCase(AdditionTest),
        unittest.TestLoader().loadTestsFromTestCase(DbOperationsTest)
    ])

    return test_suite

