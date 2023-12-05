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
                elif element == "*":
                    result_line.append(-3)
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


def find_gear(mat, i, j):
    list_gear_pos = []
    for row_idx in [-1, 0, 1]:
        for col_idx in [-1, 0, 1]:
            try:
                if mat[i+row_idx, j+col_idx] == -3:
                    list_gear_pos.append([i+row_idx, j+col_idx])
            except BaseException:
                pass
    return list_gear_pos


def remove_list_duplicates(my_list):
    s = []
    for i in my_list:
        if i not in s:
            s.append(i)
    return s


def find_gear_around(mat, row_idx, list_col_indexes):
    list_gear_pos = []
    for col_idx in list_col_indexes:
        if len(find_gear(mat, row_idx, col_idx)) > 0:
            for pos in find_gear(mat, row_idx, col_idx):
                list_gear_pos.append(pos)
        else:
            pass
    return remove_list_duplicates(list_gear_pos)


def gear_row_sum(mat: np.matrix, row_idx: int, mat_gear_agg, mat_gear_dot) -> int:
    _, n_col = mat.shape
    numbers = []
    indexes = []
    for k in range(n_col):
        if mat[row_idx, k] >= 0:
            numbers.append(mat[row_idx, k])
            indexes.append(k)
        if mat[row_idx, k] < 0 and len(numbers) > 0:
            gear_positions = find_gear_around(mat, row_idx, indexes)
            for gear_pos in gear_positions:
                mat_gear_agg[gear_pos[0], gear_pos[1]] += 1
                mat_gear_dot[gear_pos[0], gear_pos[1]] *= convert_int_list_to_int(numbers)
            numbers = []
            indexes = []
    if len(numbers) > 0:
        gear_positions = find_gear_around(mat, row_idx, indexes)
        for gear_pos in gear_positions:
            mat_gear_agg[gear_pos[0], gear_pos[1]] += 1
            mat_gear_dot[gear_pos[0], gear_pos[1]] *= convert_int_list_to_int(numbers)
    return mat_gear_agg, mat_gear_dot


def extract_gear_idx(matrix):
    row_idx, col_idx = np.where(matrix == 2)
    list_idx = []
    for k in range(row_idx.shape[0]):
        list_idx.append([row_idx[k], col_idx[k]])
    return list_idx


def gear_sum(mat: np.matrix):
    mat_gear_agg, mat_gear_sum = np.zeros((140, 140)), np.ones((140, 140))
    n_rows, n_col = mat.shape
    for k in range(n_rows):
        mat_gear_agg, mat_gear_sum = gear_row_sum(mat, k, mat_gear_agg, mat_gear_sum)
    list_pos = extract_gear_idx(mat_gear_agg)
    result = 0
    for pos in list_pos:
        result += mat_gear_sum[pos[0], pos[1]]
    return result


if __name__ == "__main__":
    with open('day3/input.txt') as f:
        lines = f.readlines()
    mat = convert_engine_schema_to_matrix(lines)
    print(gear_sum(mat))
