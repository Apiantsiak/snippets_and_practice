def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ""
    count = 0
    concat_words = []
    while count != n - k + 1:
        concat_words.append("".join(strarr[count:k + count]))
        count += 1
    ls = [(pos, len(word)) for pos, word in enumerate(concat_words)]
    index = 0
    for pos, length in ls:
        word = concat_words[index]
        if len(word) < length:
            index = pos
    return concat_words[index]


if __name__ == '__main__':
    print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
