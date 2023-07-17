from string import ascii_lowercase


def is_pangram(s):
    chars = {char for char in s.lower() if char in ascii_lowercase}
    print(chars)
    return len(ascii_lowercase) == len(chars)


if __name__ == '__main__':
    print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
