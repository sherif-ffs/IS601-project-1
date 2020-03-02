from calculator import Calculator
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

    def test_calc_multiply(self):
        calc = Calculator()
        assert calc.multiply(2) == 0
    
    def test_calc_multiply_fail(self):
        calc = Calculator()
        assert calc.multiply(0) == 0

    def test_calc_divide(self):
        calc = Calculator()
        assert calc.divide(9) == 0

    def test_calc_divide_fail(self):
        calc = Calculator()
        assert calc.divide(4) == 0

    def test_calc_square(self):
        calc = Calculator()
        assert calc.square(5) == 25
    
    def test_calc_square(self):
        calc = Calculator()
        assert calc.square(5) != 5

    def test_calc_squareRoot(self):
        calc = Calculator()
        assert calc.squareRoot(16) == 4
    
    def test_calc_squareRoot_fail(self):
        calc = Calculator()
        assert calc.squareRoot(16) != 2