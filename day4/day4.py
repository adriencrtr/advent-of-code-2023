"""
Day 2 of AOC : https://adventofcode.com/2023/day/2
"""
from typing import List


def extract_list(winning_numbers: str) -> List[str]:
    winning_numbers = winning_numbers.split('\n')[0]
    (l1, l2) = (
        winning_numbers.split(': ')[1].split(' | ')[0].split(' '),
        winning_numbers.split(': ')[1].split(' | ')[1].split(' ')
    )
    l1 = list(filter(lambda a: a != '', l1))
    l2 = list(filter(lambda a: a != '', l2))
    return (l1, l2)


def get_points_from_list(l1: List[str], l2: List[str]) -> int:
    n_common = len(list(set(l1).intersection(l2)))
    if n_common == 0:
        return 0
    return 2**(n_common-1)


def get_points(line_winning_numbers: List[str]) -> int:
    result = 0
    for winning_numbers in line_winning_numbers:
        (l1, l2) = extract_list(winning_numbers)
        result += get_points_from_list(l1, l2)
    return result


def get_total_scratch(line_winning_numbers: List[str]) -> int:
    result = {i: 1 for i in range(1, len(line_winning_numbers) + 1)}
    for idx, winning_numbers in enumerate(line_winning_numbers):
        (l1, l2) = extract_list(winning_numbers)
        n_common = len(list(set(l1).intersection(l2)))
        for _ in range(result[idx+1]):
            for k in range(n_common):
                try:
                    result[idx + k + 2] += 1
                except BaseException:
                    pass
    return sum(result.values())


if __name__ == "__main__":
    with open('day4/input.txt') as f:
        lines = f.readlines()
    print(get_total_scratch(lines))
