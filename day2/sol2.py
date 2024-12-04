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


def can_be_safe_with_dampener(report):
    if is_safety(report):
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safety(modified_report):
            return True

    return False

def solve(lines: list) -> int:
    count = 0
    for index in range(len(lines)):
        if can_be_safe_with_dampener(lines[index]):
            count += 1

    return count


lines = read_file("data.txt")
print(solve(lines))
