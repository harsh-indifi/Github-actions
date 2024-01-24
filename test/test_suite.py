import unittest

from test.tests_addition import AdditionTest


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTests([
        unittest.TestLoader().loadTestsFromTestCase(AdditionTest)
    ])

    return test_suite

