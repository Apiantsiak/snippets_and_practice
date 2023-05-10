from typing import List


def bubble_sort(arr: List[int]):
    """sort items in array with bubble method"""
    n = len(arr)
    for bypass in range(1, n):
        for k in range(0, n - bypass):
            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]
