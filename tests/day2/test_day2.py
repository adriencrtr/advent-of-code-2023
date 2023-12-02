from day2.day2 import (
    check_max_cube,
    get_game_id,
    get_max_power,
    get_sum,
    get_values,
    max_cubes_in_games,
    split_games
)


import pytest


@pytest.mark.parametrize(
        "games, expected",
        [
            ('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', [
                '3 blue, 4 red',
                '1 red, 2 green, 6 blue',
                '2 green'
            ]),
            ('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue', [
                '1 blue, 2 green',
                '3 green, 4 blue, 1 red',
                '1 green, 1 blue'
            ]),
            ('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red', [
                '8 green, 6 blue, 20 red',
                '5 blue, 4 red, 13 green',
                '5 green, 1 red'
            ]),
            ('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red', [
                '1 green, 3 red, 6 blue',
                '3 green, 6 red',
                '3 green, 15 blue, 14 red'
            ]),
            ('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green', [
                '6 red, 1 blue, 3 green',
                '2 blue, 1 red, 2 green'
            ])
        ]
)
def test_split_games(games, expected):
    assert split_games(games) == expected


@pytest.mark.parametrize(
        "game, expected",
        [
            ('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', 1),
            ('Game 23: 5 green, 8 red, 1 blue; 2 red, 5 blue, 3 green', 23)
        ]
)
def test_get_game_id(game, expected):
    assert get_game_id(game) == expected


@pytest.mark.parametrize(
        "game, expected",
        [
            ('8 green, 6 blue, 20 red', {'green': 8, 'blue': 6, 'red': 20}),
            ('5 green, 1 red', {'green': 5, 'blue': 0, 'red': 1})
        ]
)
def test_get_values(game, expected):
    assert get_values(game) == expected


@pytest.mark.parametrize(
        "games, expected",
        [
            (
                'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
                {'green': 2, 'blue': 6, 'red': 4}
            ),
            (
                'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
                {'green': 3, 'blue': 4, 'red': 1}
            ),
            (
                'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
                {'green': 13, 'blue': 6, 'red': 20}
            ),
            (
                'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
                {'green': 3, 'blue': 15, 'red': 14}
            ),
            (
                'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
                {'green': 3, 'blue': 2, 'red': 6}
            ),
        ]
)
def test_max_cubes_in_games(games, expected):
    assert max_cubes_in_games(games) == expected


@pytest.mark.parametrize(
        "cube, max_cube, expected",
        [
            ({'green': 2, 'blue': 6, 'red': 4}, {'blue': 14, 'red': 12, 'green': 13}, True),
            ({'green': 3, 'blue': 4, 'red': 1}, {'blue': 14, 'red': 12, 'green': 13}, True),
            ({'green': 13, 'blue': 6, 'red': 20}, {'blue': 14, 'red': 12, 'green': 13}, False),
            ({'green': 3, 'blue': 15, 'red': 14}, {'blue': 14, 'red': 12, 'green': 13}, False),
            ({'green': 3, 'blue': 2, 'red': 6}, {'blue': 14, 'red': 12, 'green': 13}, True),
        ]
)
def test_check_max_cube(cube, max_cube, expected):
    assert check_max_cube(cube, max_cube) == expected


@pytest.mark.parametrize(
        "game, max_cube, expected",
        [
            (
                [
                    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
                    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
                    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
                    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
                    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
                ],
                {'blue': 14, 'red': 12, 'green': 13},
                8
            ),
        ]
)
def test_get_sum(game, max_cube, expected):
    assert get_sum(game, max_cube) == expected


@pytest.mark.parametrize(
        "game, expected",
        [
            (
                [
                    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
                    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
                    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
                    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
                    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
                ],
                2286
            ),
        ]
)
def test_get_max_power(game, expected):
    assert get_max_power(game) == expected
