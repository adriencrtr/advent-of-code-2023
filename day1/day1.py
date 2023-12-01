"""
Day 1 of AOC : https://adventofcode.com/2023/day/1
"""
from typing import List


import regex as re


def extract_int_from_line(line: str) -> List[str]:
    list_int = re.findall(
        r'\d+|one|two|three|four|five|six|seven|eight|nine',
        line,
        overlapped=True
    )
    return [list_int[0], list_int[-1]]


def convert_to_int(str_int: str, first: bool) -> int:
    dict_int = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    if str_int in dict_int:
        return dict_int[str_int]
    if first:
        return int(str_int[0])
    return int(str_int[-1])


def calibration_value(line: str) -> int:
    extracted_ints = extract_int_from_line(line)
    return convert_to_int(extracted_ints[0], True)*10 + convert_to_int(extracted_ints[-1], False)


def sum_digits(list_line: List[str]) -> int:
    res_sum = 0
    for line in list_line:
        res_sum += calibration_value(line)
    return res_sum


if __name__ == "__main__":
    with open('day1/input.txt') as f:
        lines = f.readlines()
    print(sum_digits(lines))
