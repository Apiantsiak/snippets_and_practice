"""Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
Note: The function accepts an integer and returns an integer"""


def square_all_digits(number):
    """
    Return a number where all digits squared
    :param number: int
    :return: int
    """
    squared_digits_ls = [str(int(digit) ** 2) for digit in str(number)]
    return int(''.join(squared_digits_ls))


def test_valid_calc():
    test_data = 981
    assert square_all_digits(39) == int(test_data)


def test_valid_type():
    number = 56781
    assert isinstance(number, int)
    assert isinstance(square_all_digits(number), int)
