"""
Day 2 of AOC : https://adventofcode.com/2023/day/2
"""
from typing import Dict, List


def split_games(games: str) -> List[str]:
    return games.split(': ')[1].split('; ')


def get_game_id(games: str) -> int:
    return int(games.split(': ')[0].split(' ')[1])


def get_values(game: str) -> Dict[str, int]:
    res_dict = {'blue': 0, 'red': 0, 'green': 0}
    for cube in game.split(', '):
        res_dict[cube.split(' ')[1]] = int(cube.split(' ')[0])
    return res_dict


def max_cubes_in_games(games: str) -> Dict[str, int]:
    dict_max_cubes = {'blue': 0, 'red': 0, 'green': 0}
    for game in split_games(games):
        values = get_values(game)
        for color in dict_max_cubes:
            if values[color] > dict_max_cubes[color]:
                dict_max_cubes[color] = values[color]
    return dict_max_cubes


def check_max_cube(cube: Dict[str, int], max_cube: Dict[str, int]) -> bool:
    for color in cube:
        if cube[color] > max_cube[color]:
            return False
    return True


def get_sum(whole_games: str, max_cube: Dict[str, int]) -> int:
    result = 0
    for games in whole_games:
        games = games.split('\n')[0]
        max_cube_game = max_cubes_in_games(games)
        if check_max_cube(max_cube_game, max_cube):
            result += get_game_id(games)
    return result


def get_max_power(whole_games: str) -> int:
    power = 0
    for games in whole_games:
        games = games.split('\n')[0]
        min_cube_game = max_cubes_in_games(games)
        power_in_game = 1
        for color in min_cube_game:
            power_in_game *= min_cube_game[color]
        power += power_in_game
    return power


if __name__ == "__main__":
    with open('day2/input.txt') as f:
        lines = f.readlines()
        print(get_sum(lines, {'blue': 14, 'red': 12, 'green': 13}))
        print(get_max_power(lines))
