THINGS = {
    'lighter': 20,
    'compass': 100,
    'fruits': 500,
    'shirt': 300,
    'thermos': 1000,
    'first aid kit': 200,
    'jacket': 600,
    'binoculars': 400,
    'fishing rod': 1200,
    'napkins': 40,
    'sandwiches': 820,
    'tent': 5500,
    'sleeping bag': 2250,
    'chewing gum': 10,
}


def available_things(weight: int) -> None:
    sorted_things = dict(sorted(THINGS.items(), key=lambda x: -x[1]))
    for key, value in sorted_things.items():
        if value <= weight:
            print(f'{key}: {value}g', end=', ')
            weight -= value
    print('bag full now.')


def main():
    while True:
        user_data = input('Enter weight: ')
        if user_data in ['q', 'Q',  'exit']:
            print('Exit...')
            break
        elif user_data.isdigit():
            weight = int(user_data) * 1000
        else:
            print('Wrong input! Enter valid number.')
            continue
        available_things(weight)


if __name__ == '__main__':
    main()
