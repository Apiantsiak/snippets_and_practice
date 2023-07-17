def middle_permutation(string):
    sort_string = "".join(sorted(string))
    mid = len(sort_string) // 2 - 1
    if not len(sort_string) % 2:
        return sort_string[mid] + (sort_string[:mid] + sort_string[mid + 1:])[::-1]
    else:
        return sort_string[mid:mid + 2][::-1] + (sort_string[:mid] + sort_string[mid + 2:])[::-1]


if __name__ == '__main__':
    print(middle_permutation('aetxnqslbzigfvjoydkwh'))
