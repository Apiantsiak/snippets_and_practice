def expanded_form(num):
    digits = str(num)
    terms = [
        digit + "0" * (len(digits) - pos) for pos, digit in enumerate(digits, 1) if digit != "0"
    ]
    return " + ".join(terms)


if __name__ == '__main__':
    print(expanded_form(73344))
