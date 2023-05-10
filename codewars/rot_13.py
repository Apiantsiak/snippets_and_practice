from string import ascii_lowercase, digits, punctuation, whitespace


def rot13(message):
    result = ""
    ascii_x2 = ascii_lowercase*2
    other_chars = f"{digits + punctuation + whitespace}"
    for lt in message:
        if lt in other_chars:
            result += lt
            continue
        index = ascii_lowercase.index(lt.lower())
        result += f"{ascii_x2[index + 13]}".upper() if lt.isupper() else f"{ascii_x2[index + 13]}"
    return result


if __name__ == '__main__':
    print(rot13('Tte! st'))
    # 'grfg', 'Returned solution incorrect for fixed string = test'
