from typing import List


def choice_sort(arr: List[int]):
    """sort items in array with choice method"""
    n = len(arr)
    for pos in range(0, n - 1):
        for j in range(pos + 1, n):
            if arr[j] < arr[pos]:
                arr[j], arr[pos] = arr[pos], arr[j]
