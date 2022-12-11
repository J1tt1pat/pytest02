##python version 3.10
import sys
sys.path.insert(0, './function')

from calculate import sum_of_two_numbers, display_error, validate_input
import pytest

def main():
    number1 = int(input("input number1:  "))
    number2 = int(input("input number2:  "))
    total = sum_of_two_numbers(number1, number2)
    print(total)

if __name__ == "__main__":
    main()