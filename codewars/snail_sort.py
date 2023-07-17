def snail_sort(array):
    result = []
    while array:
        result.extend(array.pop(0))
        for row in array:
            result.append(row.pop())
        if array:
            result.extend(array.pop()[::-1])
        for row in array[::-1]:
            result.append(row.pop(0))
    return result


if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 1],
        [4, 5, 6, 4],
        [7, 8, 9, 7],
        [7, 8, 9, 7],
    ]
    print(snail_sort(matrix))
