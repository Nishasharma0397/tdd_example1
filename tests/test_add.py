"""
program for calculator
"""
import calculator  # Imports the calculator module (calculator.py)

def test_two_plus_two():
    """
    Asserts that given the parameters 2 and 2, the add
    function should return 4.
    """
    assert calculator.add(2, 2) == 4

def test_five_plus_seven():
    """
    Asserts that given the parameters 5 and 7, the add
    function should return 12.
    """
    assert calculator.add(5, 7) == 12

def test_no_parameters():
    """
    Asserts that when no parameters are provided,
    0 should be returned.
    """
    assert calculator.add() == 0

def test_with_three_arguments():
    """
    Asserts that when 123,
    6 should be returned.
    """
    assert calculator.add(1, 2, 3) == 6


def test_with_five_arguments():
    """
    Asserts that when 12345,
    15 should be returned.
    """
    assert calculator.add(1, 2, 3, 4, 5) == 15
