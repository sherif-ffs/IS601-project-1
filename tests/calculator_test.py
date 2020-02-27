from calculator import Calculator
import pytest 
import unittest

class test_calculator(unittest.TestCase):

    def test_calc(self):
        calc = Calculator()
        assert calc

    def test_calc_add(self):
        calc = Calculator()
        assert calc.add(2) == 2

    def test_calc_add_fail(self):
        calc = Calculator()
        assert calc.add(2) != 3

    def test_calc_subtract(self):
        calc = Calculator()
        assert calc.subtract(5) != -5

    def test_calc_subtract_fail(self):
        calc = Calculator()
        assert calc.subtract(2) != 5

