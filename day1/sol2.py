from day1.sol1 import LEFT, RIGHT


def solve2(left, right):
    result = 0
    point = 0
    while point < len(left) and point < len(right):
        left_int = left[point]
        count_in_right = right.count(left_int)
        result += abs(int(left_int) * int(count_in_right))
        point += 1
    return result


print(solve2(LEFT, RIGHT))
