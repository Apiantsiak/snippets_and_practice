def wave(s):
    # result = []
    # for ind, lt in enumerate(people):
    #     if lt == " ":
    #         continue
    #     word_items = list(people)
    #     word_items[ind] = lt.upper()
    #     result.append("".join(word_items))
    # return ", ".join(result)
    return [s[:i] + s[i:].capitalize() for i in range(len(s)) if s[i] != " "]


if __name__ == '__main__':
    print(wave("two words"))
