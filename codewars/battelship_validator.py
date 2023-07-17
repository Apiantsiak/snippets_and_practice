def validate_battlefield(field):
    return battle(
        set(
            [(r, c) for c in range(10) for r in range(10) if field[r][c]]
        ),
        [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
    )


def battle(grid, fleet):
    return sum(fleet) == len(grid) and \
        (fleet == [] or any(battle(grid - p, fleet[:-1]) for p in possibles(grid, fleet[-1])))


def possibles(grid, ship):
    return [
        set(p) for p in
        [
            [
                (r + i, c) for i in range(ship)
            ] for r, c in grid] + [
            [
                (r, c + i) for i in range(ship)
            ] for r, c in grid
        ]
        if set(p) <= grid
    ]


if __name__ == '__main__':
    print(validate_battlefield(
        [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
         [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))
