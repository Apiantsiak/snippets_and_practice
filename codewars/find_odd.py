"""Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd)."""


from collections import Counter


def calc_odd_occurs(array):
    """
    Find the one that appears an odd number of times un an given array
    :param array: list
    :return: int
    """
    counted_digit = Counter(array)
    for key, value in counted_digit.items():
        if value % 2:
            return key


def test_calculation():
    assert calc_odd_occurs([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]) == 4
    assert calc_odd_occurs([1, 1, 2]) == 2
    assert calc_odd_occurs([0, 1, 0, 1, 0]) == 0
