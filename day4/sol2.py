from copy import deepcopy

from day4.sol1 import rotate_matrix_90, read_data


def find_xmas(data):
    matrix = deepcopy(data)
    count = 0
    patterns = ["MAS", "SAM"]
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            mas_1 = matrix[i - 1][j - 1] + matrix[i][j] + matrix[i + 1][j + 1]
            mas_2 = matrix[i + 1][j - 1] + matrix[i][j] + matrix[i - 1][j + 1]

            if mas_1 in patterns and mas_2 in patterns:
                count += 1
    return count


if __name__ == '__main__':
    data = read_data("data.txt")
    amount = find_xmas(data)
    print("Liczba wystąpień X-MAS:", amount)
