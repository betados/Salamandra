# -*- coding: utf-8 -*-

import unittest
from vector import *
import math


class TestVector(unittest.TestCase):
    def test_get_next_two_divs(self):
        self.assertEqual(Vector(0, 1), VectorPolar(1, math.pi / 2.0).to_cartesian())
        self.assertEqual(Vector(1, 0), VectorPolar(1, 0).to_cartesian())
