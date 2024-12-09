import re
import typing
from copy import deepcopy


def read_data(filename):
    with open(filename) as file:
        data = file.read()
    return list(map(list, data.split()))


def make_data_as_text(data):
    text = ""
    for row in data:
        text += "".join(row)
        text += "\n"
    return text


def get_main_diagonals(matrix):
    rows, cols = len(matrix), len(matrix[0])
    diagonals = {}

    for row_i in range(rows):
        for col_i in range(cols):
            diagonal_identifier = row_i - col_i
            if diagonal_identifier not in diagonals:
                diagonals[diagonal_identifier] = []
            diagonals[diagonal_identifier].append(matrix[row_i][col_i])

    return [diagonals[d] for d in sorted(diagonals.keys())]


def solve(data: typing.List[list], pattern: str = r"XMAS"):
    matrix = deepcopy(data)
    rotate_right_1 = rotate_matrix_90(matrix)
    rotate_right_2 = rotate_matrix_90(rotate_right_1)
    rotate_right_3 = rotate_matrix_90(rotate_right_2)
    matrices = [matrix, rotate_right_1, rotate_right_2, rotate_right_3]
    amount = 0
    for d in matrices:
        main_diagonals = get_main_diagonals(d)
        matrix_text = make_data_as_text(d)
        main_diagonals_text = make_data_as_text(main_diagonals)
        amount += len(re.findall(pattern, matrix_text))
        amount += len(re.findall(pattern, main_diagonals_text))
    return amount


def rotate_matrix_90(matrix):
    transposed = list(zip(*matrix))
    rotated = [list(row)[::-1] for row in transposed]
    return rotated


if "__main__" == __name__:
    data = read_data("data.txt")
    solve(data)
