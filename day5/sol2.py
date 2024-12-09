import typing

from day5.sol1 import read_data


def organized_updates(page_numbers: typing.List[str], rules: typing.DefaultDict[str, typing.List[str]]) -> typing.List[
    str]:
    """
    Reorganizes a sequence of page numbers to satisfy the given ordering rules.
    """
    page_nums_copy = page_numbers.copy()
    changed = True

    while changed:
        changed = False
        for i in range(len(page_nums_copy) - 1):
            page_number = page_nums_copy[i]
            rest_nums = page_nums_copy[i + 1:]
            for j, num in enumerate(rest_nums):
                if page_number in rules[num]:
                    page_nums_copy.pop(i)
                    page_nums_copy.insert(i + j + 1, page_number)
                    changed = True
                    break
            if changed:
                break

    return page_nums_copy


def sol2(page_numbers_col: typing.List[typing.List[str]], rules: typing.DefaultDict[str, typing.List[str]]) -> int:
    """
    Processes multiple sequences, validates, and sums up the middle numbers of reorganized sequences.
    """
    count = 0
    for page_numbers in page_numbers_col:
        is_correct = True
        for i in range(len(page_numbers) - 1):
            if page_numbers[i + 1] not in rules[page_numbers[i]]:
                is_correct = False
                break

        if not is_correct:
            print(page_numbers)
            corrected_sequence = organized_updates(page_numbers, rules)
            mid = corrected_sequence[len(corrected_sequence) // 2]
            count += int(mid)
    print(count)
    return count


if __name__ == "__main__":
    filename = "data.txt"
    page_numbers_col, rules = read_data(filename)
    sol2(page_numbers_col, rules)
