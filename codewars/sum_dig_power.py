def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function
    dct = {
        num: sum([int(i) ** pos for pos, i in enumerate(str(num), 1)])
        for num in range(a, b + 1)
    }
    return [key for key, val in dct.items() if key == val]


if __name__ == '__main__':
    print(sum_dig_pow(1, 100))
