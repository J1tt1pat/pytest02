##python version 3.10
import sys
sys.path.insert(0, './function')

from calculate import sum_of_two_numbers, display_error, validate_input
import pytest

@pytest.mark.parametrize('number1, number2, expected_result',
[
    (1,3,4),
    (2,3,5),
    (2,-3,-1),
    (-2,-3,-5),
    (1.5,3.2,4.7),
    (1.5,-2.0,-0.5),
    ("", 8, "input number1 again"),
    (8, "", "input number2 again")

])

def test_sum_of_of_two_numbers(number1, number2, expected_result):
    actual_result = sum_of_two_numbers(number1, number2)
    assert expected_result == actual_result

@pytest.mark.parametrize('number, expected_result',
[
    ("", False),
    (1, True)
])

def test_validate_input(number, expected_result):
    actual_result = validate_input(number)
    assert expected_result == actual_result

@pytest.mark.parametrize('index, expected_result',
[
    (1, "input number1 again"),
    (2, "input number2 again")
])

def test_display_error(index, expected_result):
    actual_result = display_error(index)
    assert expected_result == actual_result