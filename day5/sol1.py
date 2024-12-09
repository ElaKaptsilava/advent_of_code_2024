import typing
from collections import defaultdict


def read_data(filename):
    with open(filename) as file:
        page_ordering_rules, update_page_numbers = file.read().split("\n\n")
        page_ordering_rules = list(map(lambda nums: nums.split("|"), page_ordering_rules.split("\n")))
        update_page_numbers = list(map(lambda nums: nums.split(","), update_page_numbers.split("\n")))
        rules = defaultdict(list)
        for rule in page_ordering_rules:
            first_page, last_page = rule
            rules[first_page].append(last_page)
        return update_page_numbers, rules


def sol1(page_numbers_col: typing.List[list], rules: typing.DefaultDict):
    count = 0
    for page_numbers in page_numbers_col:
        is_correct = True
        for i in range(0, len(page_numbers)-1):
            page_number, next_number = page_numbers[i], page_numbers[i + 1]
            if next_number not in rules[page_number]:
                is_correct = False
                break
        if is_correct:
            mid = page_numbers[len(page_numbers)//2]
            count += int(mid)
    return count


if __name__ == "__main__":
    filename = "data.txt"
    page_numbers_col, rules = read_data(filename)
    sol1(page_numbers_col, rules)
