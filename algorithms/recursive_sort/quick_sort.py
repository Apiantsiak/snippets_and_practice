"""O(n^2) worst case
O(n*log(n)) best and average case

Quick sort
     1. Choose pivot element (Usually last or random)
     2. Stores elements less than pivot in left subarray
        Stores elements greater than pivot in right subarray
     3. Call quicksort recursively on left subarray"""


def quick_sort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quick_sort(arr, left, partition_pos - 1)
        quick_sort(arr, partition_pos + 1, right)


def partition(arr, left, right):
    i = left
    j = right
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i


if __name__ == '__main__':
    test_arr = []
    quick_sort(test_arr, 0, len(test_arr) - 1)
    print(test_arr)
