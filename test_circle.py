"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import unittest
import math

class Test(unittest.TestCase):

    def setUp(self):
        self.circle = Circle(7)

    def test_add_area_normal(self):
        new_circle = Circle(7)
        added_circle = self.circle.add_area(new_circle)
        self.assertEqual(math.sqrt(98), added_circle.get_radius())
        self.assertEqual(math.pi*98, added_circle.get_area())

    def test_add_0_radius_circle(self):
        new_circle = Circle(0)
        added_circle = self.circle.add_area(new_circle)
        self.assertEqual(self.circle.get_radius(), added_circle.get_radius())
        self.assertEqual(self.circle.get_area(), added_circle.get_area())

    def negative_circle(self):
        with self.assertRaises(ValueError):
            new_circle = Circle(-1)


