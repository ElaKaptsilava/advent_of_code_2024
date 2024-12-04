"""
  - The levels are either all "increasing" or all "decreasing".
  - Any two adjacent levels differ by at least 1, 2,3 .
"""


def read_file(file_name: str) -> list:
    with open(file_name, "r") as file:
        data = []
        for line in file.readlines():
            line = list(map(int, line.split()))
            data.append(line)

    return data


def is_safety(report: list) -> bool:
    increasing = None
    for index in range(len(report) - 1):
        diff = abs(report[index] - report[index + 1])

        if diff < 1 or diff > 3:
            return False

        if increasing is None:
            increasing = report[index] < report[index + 1]
        elif increasing != (report[index] < report[index + 1]):
            return False

    return True


def solve(lines: list) -> int:
    count = 0
    for index in range(len(lines)):
        if is_safety(lines[index]):
            count += 1

    return count


lines = read_file("data.txt")
print(solve(lines))

"""
7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
"""
