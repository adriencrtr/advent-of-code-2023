from day1.day1 import (
    extract_int_from_line,
    convert_to_int,
    calibration_value,
    sum_digits
)


import pytest


@pytest.mark.parametrize(
        "test_input, expected",
        [
            ('1abc2', ['1', '2']),
            ('pqr3stu8vwx', ['3', '8']),
            ('a1b2c3d4e5f', ['1', '5']),
            ('treb7uchet', ['7', '7']),
            ('two1nine', ['two', 'nine']),
            ('eightwothree', ['eight', 'three']),
            ('abcone2threexyz', ['one', 'three']),
            ('xtwone3four', ['two', 'four']),
            ('4nineeightseven2', ['4', '2']),
            ('zoneight234', ['one', '4']),
            ('7pqrstsixteen', ['7', 'six']),
            ('2911threeninesdvxvheightwobm', ['2911', 'two']),
        ]
)
def test_extract_int_from_line(test_input, expected):
    assert extract_int_from_line(test_input) == expected


@pytest.mark.parametrize(
        "str_int, first, expected",
        [
            ('1', True, 1),
            ('1', False, 1),
            ('nine', True, 9),
            ('nine', False, 9),
            ('2911', True, 2),
            ('2911', False, 1)
        ]
)
def test_convert_to_int(str_int, first, expected):
    assert convert_to_int(str_int, first) == expected


@pytest.mark.parametrize(
        "line, expected",
        [
            ('two1nine', 29),
            ('2911threeninesdvxvheightwobm', 22)
        ]
)
def test_calibration_value(line, expected):
    assert calibration_value(line) == expected


@pytest.mark.parametrize(
        "list_line, expected",
        [
            (['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet'], 142),
            ([
                'two1nine',
                'eightwothree',
                'abcone2threexyz',
                'xtwone3four',
                '4nineeightseven2',
                'zoneight234',
                '7pqrstsixteen'
            ], 281),
        ]
)
def test_sum_digits(list_line, expected):
    assert sum_digits(list_line) == expected
