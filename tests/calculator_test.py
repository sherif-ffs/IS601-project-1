def test_calc_add():
    from calculator import Calculator
    calc = Calculator()
    assert calc.add(2,2) == 4

def test_calc_add_fail():
    from calculator import Calculator
    calc = Calculator()
    assert calc.add(5,2) != 3
