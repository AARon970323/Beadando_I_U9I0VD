from src.calculator import Calculator

def test_complex_flow():
    calc = Calculator()
    result = calc.add(5, 5)
    result = calc.divide(result, 2)
    assert result == 5
