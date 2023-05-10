"""Your task is to make a function that can take any non-negative integer as an argument and return
it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
Examples:
Input: 42145 Output: 54421
Input: 145263 Output: 654321
Input: 123456789 Output: 987654321"""


def highest_pos_num(number):
    """
    Return digits of number in descending order
    :param number: int
    :return: int
    """
    digits_ls = sorted(list(str(number)), reverse=True)
    return int(''.join(digits_ls))


if __name__ == '__main__':
    print(highest_pos_num(input('Enter your number: ')))
