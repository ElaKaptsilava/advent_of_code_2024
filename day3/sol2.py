import re

from day3.sol1 import read_data


def solve2(data: str) -> int:
    mul_pattern, control_pattern = r"mul\((\d{1,3}),(\d{1,3})\)", r"(do\(\)|don't\(\))"
    instructions = re.finditer(f"{control_pattern}|{mul_pattern}", data)
    safety = []
    is_enable = True
    for instruction in instructions:
        instruction_groups = instruction.groups()
        mul1, mul2 = instruction_groups[1], instruction_groups[2]
        if "don't()" in instruction_groups:
            is_enable = False
        elif "do()" in instruction_groups:
            is_enable = True
        if is_enable and mul1 is not None and mul2 is not None:
            multiply_mul = int(mul1) * int(mul2)
            safety.append(multiply_mul)
    return sum(safety)


data = read_data("data.txt")

if __name__ == "__main__":
    print(solve2(data))
