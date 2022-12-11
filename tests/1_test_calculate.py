##python version 3.10
import sys
sys.path.insert(0, './function')

from calculate import sum_of_two_numbers
from calculate import display_error
from calculate import validate_input
import pytest

def test_true4_sum_two_number():
    number1 = 1
    number2 = 3
    expected_result = 4
    actual_result = sum_of_two_numbers(number1, number2)
    assert expected_result == actual_result

def test_true5_sum_two_number():
    number1 = 2
    number2 = 3
    expected_result = 5
    actual_result = sum_of_two_numbers(number1, number2)
    assert expected_result == actual_result

def test_true_minus1_sum_two_number():
    number1 = 2
    number2 = -3
    expected_result = -1
    actual_result = sum_of_two_numbers(number1, number2)
    assert expected_result == actual_result

def test_true_minus5_sum_two_number():
    number1 = -2
    number2 = -3
    expected_result = -5
    actual_result = sum_of_two_numbers(number1, number2)
    assert expected_result == actual_result

def test_true_decimal_4_point_7_sum_two_number():
    number1 = 1.5
    number2 = 3.2
    expected_result = 4.7
    actual_result = sum_of_two_numbers(number1, number2)
    assert expected_result == actual_result

def test_true_minus_decimal_0_point_5_sum_two_number():
    number1 = 1.5
    number2 = -2.0
    expected_result = -0.5
    actual_result = sum_of_two_numbers(number1, number2)
    assert expected_result == actual_result

def test_fail_input01_sum_two_number():
    number1 = ""
    number2 = 8
    expected_result = "input number1 again"
    actual_result = sum_of_two_numbers(number1, number2)
    assert expected_result == actual_result

def test_fail_input02_sum_two_number():
    number1 = 8
    number2 = ""
    expected_result = "input number2 again"
    actual_result = sum_of_two_numbers(number1, number2)
    assert expected_result == actual_result

def test_false_validate_input_string():
    input = ""
    expected_result = False
    actual_result = validate_input(input)
    assert expected_result == actual_result

def test_true_validate_input_string():
    input = 1
    expected_result = True
    actual_result = validate_input(input)
    assert expected_result == actual_result

def test_show_string_display_error_index1():
    index = 1
    expected_result = "input number"+str(index)+" again"
    actual_result = display_error(index)
    assert expected_result == actual_result

def test_show_string_display_error_index2():
    index = 2
    expected_result = "input number"+str(index)+" again"
    actual_result = display_error(index)
    assert expected_result == actual_result