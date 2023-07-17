def count_smileys(arr):
    valid_tokens = [":;", "-~", ")D"] if len(arr) > 2 else  [":;", "-~", ")D"]
    res = []
    for smile in arr:
        check = 1
        for pos, token in enumerate(smile):
            if token in valid_tokens[pos]:
                continue
            else:
                check = 0
        if check:
            res.append(smile)
    return len(res)


if __name__ == '__main__':
    count_smileys([':D', ':~)', ';~D', ':)'])
