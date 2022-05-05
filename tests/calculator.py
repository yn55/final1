"""Testing the Calculator"""
from calculator import Calculator


def test_calculator_is_instance():
    """Testing the Calculator"""
    calculator = Calculator()
    assert isinstance(calculator, Calculator)

def test_calculator_get_result_method():
    """Testing the Calculator"""
    calculator = Calculator()
    assert calculator.get_result() == 0