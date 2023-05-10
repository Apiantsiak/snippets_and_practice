from random import randint
from typing import List, NoReturn

test_arr = [randint(0, 10) for i in range(10)]


# O(n^2)
def insert_sort(arr: List[int]) -> NoReturn:
    """ sort array with insert method"""
    n = len(arr)
    for i in range(1, n):
        index = i
        while index > 0 and arr[index - 1] > arr[index]:
            arr[index - 1], arr[index] = arr[index], arr[index - 1]
            index -= 1


if __name__ == '__main__':
    built_sort = sorted(test_arr)
    insert_sort(test_arr)
    assert test_arr == built_sort
