import re


def read_data(file_name):
    with open(file_name, "r") as file:
        data = file.read()
    return data


def solve1(data: str) -> int:
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    find_all_mul = re.findall(pattern, data)
    multiply_mul_func = lambda int_str: int(int_str[0]) * int(int_str[1])
    multiply_mul = list(map(multiply_mul_func, find_all_mul))
    return sum(multiply_mul)


data = read_data("data.txt")
if __name__ == "__main__":
    print(solve1(data))
