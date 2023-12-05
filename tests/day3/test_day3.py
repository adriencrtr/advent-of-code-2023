from day3.day3 import (
    convert_engine_schema_to_matrix,
    convert_int_list_to_int,
    row_sum,
    is_adjacent,
    is_number_adjacent
)

import numpy as np


import pytest

MY_MATRIX = (
    np.matrix([
                    [4, 6, 7, -1, -1, 1, 1, 4, -1, -1],
                    [-1, -1, -1, -2, -1, -1, -1, -1, -1, -1],
                    [-1, -1, 3, 5, -1, -1, 6, 3, 3, -1],
                    [-1, -1, -1, -1, -1, -1, -2, -1, -1, -1],
                    [6, 1, 7, -2, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -2, -1, 5, 8, -1],
                    [-1, -1, 5, 9, 2, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1, 7, 5, 5, -1],
                    [-1, -1, -1, -2, -1, -2, -1, -1, -1, -1],
                    [-1, 6, 6, 4, -1, 5, 9, 8, -1, -1]
                ])
)


@pytest.mark.parametrize(
        "schema, expected",
        [
            (
                [
                    '467..114..\n',
                    '...*......\n',
                    '..35..633.\n',
                    '......#...\n',
                    '617*......\n',
                    '.....+.58.\n',
                    '..592.....\n',
                    '......755.\n',
                    '...$.*....\n',
                    '.664.598..\n'
                ],
                MY_MATRIX
            )
        ]
)
def test_convert_engine_schema_to_matrix(schema, expected):
    assert np.array_equal(convert_engine_schema_to_matrix(schema), expected)


@pytest.mark.parametrize(
        "list_int, expected",
        [
            ([4, 6, 7], 467),
            ([2], 2),
            ([5, 0, 4, 7], 5047),
        ]
)
def test_convert_int_list_to_int(list_int, expected):
    assert convert_int_list_to_int(list_int) == expected


@pytest.mark.parametrize(
        "matrix, i, j, expected",
        [
            (MY_MATRIX, 0, 0, False)
        ]
)
def test_is_adjacent(matrix, i, j, expected):
    assert is_adjacent(matrix, i, j) == expected


@pytest.mark.parametrize(
        "matrix, i, list_idx, expected",
        [
            (MY_MATRIX, 5, [7, 8], False)
        ]
)
def test_is_number_adjacent(matrix, i, list_idx, expected):
    assert is_number_adjacent(matrix, i, list_idx) == expected


@pytest.mark.parametrize(
        "matrix, i, expected",
        [
            (MY_MATRIX, 0, 467),
            (MY_MATRIX, 1, 0),
            (MY_MATRIX, 2, 668),
            (MY_MATRIX, 3, 0),
            (MY_MATRIX, 4, 617),
            (MY_MATRIX, 5, 0),
            (MY_MATRIX, 6, 592),
            (MY_MATRIX, 7, 755),
            (MY_MATRIX, 8, 0),
            (MY_MATRIX, 9, 1262),
        ]
)
def test_row_sum(matrix, i, expected):
    assert row_sum(matrix, i) == expected
