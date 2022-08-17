from typing import Dict


def write_sales_data(turns):
    sales_data: Dict[str, Dict[str, int]] = {}
    for _ in range(turns):
        name, item, quantity = input('Enter "name, item, quantity": ').split(',')
        sales_data[name][item] = sales_data.setdefault(name.strip(), {}).setdefault(item.strip(), int(quantity))
    print('This records were saved:')
    for key, value in sales_data.items():
        for item, quantity in value.items():
            print(f'{key.capitalize()}:\n{item.capitalize()} {quantity}')


def main():
    count = 0
    while True:
        prompt = 'Enter number of records or enter "q" for quit: ' if not count else 'Continue or enter "q" for quit: '
        user_data = input(prompt)
        if user_data in ['q', 'Q']:
            print('Exit bye...')
            break
        write_sales_data(int(user_data))
        count += 1


if __name__ == '__main__':
    main()
