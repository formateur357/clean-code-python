from src import calc
import pytest

def test_add_two_numbers():
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 4) == 3

def test_sub_two_numbers():
    assert calc.sub(10, 3) == 7
    assert calc.sub(3, 10) == -7


def test_apply_rate_basic(default_rate):
    assert calc.apply_rate(100.0, default_rate) == 120

def test_apply_require_positive_rate():
    with pytest.raises(ValueError):
        calc.apply_rate(100.0, 0)
    with pytest.raises(ValueError):
        calc.apply_rate(100.0, -1.0)


def test_counter_starts_at_fixture_value(start_value):
    c = calc.Counter(start_value)
    assert c.value == start_value

def test_counter_increment(start_value):
    c = calc.Counter(start_value)
    c.increment(); c.increment()
    assert c.value == start_value + 2

def test_counter_reset(start_value):
    c = calc.Counter(start_value)
    c.increment(); c.increment()
    c.reset()
    assert c.value == start_value