##python version 3.10
def sum_of_two_numbers(number1, number2):
    if not validate_input(number1):
        return display_error(1)
    elif not validate_input(number2):
        return display_error(2)
    else: return number1+number2

def display_error(index):
    return "input number"+str(index)+" again"

def validate_input(number):
    if isinstance(number, int) or isinstance(number, float): valid_input = True
    elif isinstance(number, str): valid_input = False
    return valid_input