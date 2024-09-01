"""
Sample tests
"""

from django.test import SimpleTestCase

from . import calc


def CalcTest(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Testing adding numbers together"""
        res = calc.add(5, 6)
        self.assertEqual(res, 131)
