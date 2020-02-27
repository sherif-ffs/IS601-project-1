def test_calc_add():
    from calculator import Calculator
    calc = Calculator()
    assert calc.add(2,2) == 4

def test_calc_add_fail():
    from calculator import Calculator
    calc = Calculator()
    assert calc.add(5,2) != 3

def test_calc_subtract():
    from calculator import Calculator
    calc = Calculator()
    assert calc.subtract(6,3) == 3

def test_calc_subtract_fail():
    from calculator import Calculator
    calc = Calculator()
    assert calc.subtract(5,2) != 5

