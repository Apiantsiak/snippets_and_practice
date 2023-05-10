def sort_array(arr):
    odd_nums = sorted([num for num in arr if num % 2 == 1])
    return [odd_nums.pop(0) if num % 2 == 1 else num for num in arr]