from random import randint
from typing import List, Optional


def get_rand_arr(arr_len: int):
    sort_arr = [randint(0, 100) for i in range(0, arr_len)]
    sort_arr.sort()
    return sort_arr


def binary_search(sort_arr: List[int], value: int) -> Optional[int]:
    first = 0
    last = len(sort_arr) - 1
    while first < last:
        middle_key = int(first + (last - first) / 2)
        middle_val = sort_arr[middle_key]
        if value < middle_val:
            last = middle_key - 1
        elif value > middle_val:
            first = middle_key + 1
        else:
            return middle_key
    return None


if __name__ == '__main__':
    val = randint(0, 100)
    arr = get_rand_arr(randint(10, 100))
    result = binary_search(arr, val)
    print(f"Search area: {arr}", f"Searching index of {val}: {result}", sep="\n")
