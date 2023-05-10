def diamond(n):
    if n % 2 == 0 or n <= 0:
        return None
    stars = [i for i in list(range(n + 1)) + list(reversed(range(n))) if i % 2]
    dimond = "".join([f"{'*' * i}".center(n) + "\n" for i in stars])
    return dimond


if __name__ == '__main__':
    print(diamond(7))
