def read_data(file_name):
    with open(file_name, "r") as file:
        read_file = file.read().split("\n")
        data = list(map(lambda x: x.split(), read_file))
        left, right = zip(*data)
        return list(left), list(right)


LEFT, RIGHT = read_data("data.txt")


def solve(left, right):
    result = 0
    while left or right:
        left_min, right_min = min(left), min(right)
        left.remove(left_min)
        right.remove(right_min)
        result += abs(int(left_min) - int(right_min))
    return result


left_copy = list(LEFT)
right_copy = list(RIGHT)
solve(left_copy, right_copy)
