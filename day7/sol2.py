from day7.sol1 import part_two, parse

if __name__ == '__main__':
    with open("data.txt") as f:
        equations = [parse(l.strip()) for l in f.readlines()]
    print(part_two(equations))
