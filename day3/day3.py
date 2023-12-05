"""
Day 2 of AOC : https://adventofcode.com/2023/day/2
"""
from typing import List


import numpy as np


def convert_engine_schema_to_matrix(engine_schema: str) -> np.matrix:
    result = []
    for line in engine_schema:
        result_line = []
        line = line.split('\n')[0]
        for element in line:
            try:
                result_line.append(int(element))
            except BaseException:
                if element == ".":
                    result_line.append(-1)
                else:
                    result_line.append(-2)
        result.append(result_line)
    return np.matrix(result)


def convert_int_list_to_int(my_list: List[int]) -> int:
    """
    Convert List to int like this :
        Example : my_list = [4, 6, 7]
        Output : 467
    """
    result = 0
    my_list.reverse()
    for idx, element in enumerate(my_list):
        result += element*(10**idx)
    return result


def is_adjacent(mat: np.matrix, i: int, j: int) -> bool:
    for row_idx in [-1, 0, 1]:
        for col_idx in [-1, 0, 1]:
            try:
                if mat[i+row_idx, j+col_idx] == -2:
                    return True
            except BaseException:
                pass
    return False


def is_number_adjacent(
        mat: np.matrix,
        row_index: int,
        list_col_indexes: List[int]
) -> bool:
    for col_idx in list_col_indexes:
        if is_adjacent(mat, row_index, col_idx):
            return True
    return False


def add_to_sum(mat: np.matrix, numbers: List[int], row_index: int, list_indexes: List[int]) -> int:
    if is_number_adjacent(mat, row_index, list_indexes):
        return convert_int_list_to_int(numbers)
    return 0


def row_sum(mat: np.matrix, row_idx: int) -> int:
    _, n_col = mat.shape
    result = 0
    numbers = []
    indexes = []
    for k in range(n_col):
        if mat[row_idx, k] >= 0:
            numbers.append(mat[row_idx, k])
            indexes.append(k)
        if mat[row_idx, k] < 0 and len(numbers) > 0:
            result += add_to_sum(mat, numbers, row_idx, indexes)
            numbers = []
            indexes = []
    if len(numbers) > 0:
        result += add_to_sum(mat, numbers, row_idx, indexes)
    return result


def get_sum(schema: str) -> int:
    scheme_matrix = convert_engine_schema_to_matrix(schema)
    n_rows, _ = scheme_matrix.shape
    result = 0
    for i in range(n_rows):
        result += row_sum(scheme_matrix, i)
    return result


def gear_row_sum(mat: np.matrix, row_idx: int, mat_gear_agg, mat_gear_sum) -> int:
    _, n_col = mat.shape
    result = 0
    numbers = []
    indexes = []
    for k in range(n_col):
        if mat[row_idx, k] >= 0:
            numbers.append(mat[row_idx, k])
            indexes.append(k)
        if mat[row_idx, k] < 0 and len(numbers) > 0:
            result += add_to_sum(mat, numbers, row_idx, indexes)
            numbers = []
            indexes = []
    if len(numbers) > 0:
        result += add_to_sum(mat, numbers, row_idx, indexes)
    return result


def gear_sum(schema):
    scheme_matrix = convert_engine_schema_to_matrix(schema)
    n_rows, n_col = scheme_matrix.shape
    mat_gear_agg = np.zeros((n_rows, n_col))
    mat_gear_sum = np.zeros((n_rows, n_col))



if __name__ == "__main__":
    with open('day3/input.txt') as f:
        lines = f.readlines()
        print(get_sum(lines))
