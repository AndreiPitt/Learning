import pytest

from file1 import get_weather, add, divide


def test_get_weather():
    assert get_weather(32) == "hot"


def test_add():
    assert add(1, 3) == 4, "1+3 should be 4"
    assert add(-1, 2) == 1, "-1+2 should be 1"
    assert add(5, -5) == 0, "5-5 should be 0"


def test_divide():
    with pytest.raises(ValueError, match="You cant divide by zero."):
        divide(5, 0)
