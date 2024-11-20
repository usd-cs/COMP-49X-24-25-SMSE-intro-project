"""
Just a sample test module.
"""
from django.test import TestCase


class SampleTest(TestCase):
    """
    Test case for a sample.
    """

    def test_sample(self):
        """
        Sample test.
        """
        self.assertEqual(1 + 1, 2)
