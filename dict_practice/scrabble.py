from string import ascii_lowercase
from typing import Dict
from time import sleep


DATA_ENG: Dict[str, int] = {
    'A, E, I, O, U, L, N, S, T, R': 1,
    'D, G': 2,
    'B, C, M, P': 3,
    'F, H, V, W, Y': 4,
    'K': 5,
    'J, X': 8,
    'Q, Z': 10,
}

DATA_RU: Dict[str, int] = {
    'А, В, Е, И, Н, О, Р, С, Т': 1,
    'Д, К, Л, М, П, У': 2,
    'Б, Г, Ё, Ь, Я': 3,
    'Й, Ы': 4,
    'Ж, З, Х, Ц, Ч': 5,
    'Ш, Э, Ю': 8,
    'Ф, Щ, Ъ': 10,
}


def count_word_score(word: str, lang: str) -> int:
    chars = list(word)
    data_type = DATA_ENG if lang == 'eng' else DATA_RU
    score = 0
    for char in chars:
        for key, value in data_type.items():
            if char.lower() in key.lower():
                score += value
    return score


def check_word(word: str) -> str:
    if word.isalpha():
        return 'eng' if word[0].lower() in ascii_lowercase else 'ru'
    else:
        print('Wrong input!')


def main():
    while True:
        user_word = input('Enter your word: ')
        if user_word.lower() == 'q':
            print('Exit...')
            break
        lang = check_word(user_word)
        result = count_word_score(user_word, lang)
        for i in range(result):
            print('>') if i == max(range(result)) else print('-', end="")
            sleep(0.1)
        print(f'Your score is {result}!')


if __name__ == '__main__':
    main()
