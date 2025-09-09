# calculator.py

def addition(a, b):
    return a + b

# test_calculator.py

from calculator import addition

def test_addition():
    assert addition(2, 3) == 5