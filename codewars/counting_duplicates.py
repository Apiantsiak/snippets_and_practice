"""Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric
digits that occur more than once in the input string.
The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"""

from collections import Counter


def count_dupl(data: str) -> int:
    counter = Counter(list(data.lower()))
    result = 0
    for key, value in counter.items():
        result += 1 if value > 1 else 0
        print(f'{key} occurs {value} times')
    return result


if __name__ == '__main__':
    assert count_dupl('Aaaa11') == 2
    assert count_dupl("aabbcde") == 2
    assert count_dupl("aabBcde") == 2
    assert count_dupl('indivisibility') == 1
