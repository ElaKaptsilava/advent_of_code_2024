def read_data(filename):
    road_map: dict = {}
    starting_positions: list[complex] = []
    with open(filename) as file:
        data = file.read()
        for row, line in enumerate(data.split('\n')):
            for column, num in enumerate(line):
                pos = complex(column, row)
                road_map[pos] = int(num)
                if not int(num):
                    starting_positions.append(pos)
    return road_map, starting_positions


def bfs_trail_score(road_map, start_pos, steps: set = (1, -1, 1j, -1j)) -> int:
    visited, reachable_nines, to_visit = set(), set(), [start_pos]
    while to_visit:
        if (current := to_visit.pop(0)) in visited:
            continue
        visited.add(current)
        current_height = road_map[current]
        for step in steps:
            if (neighbor := current + step) in road_map:
                if (neighbor_height := road_map[neighbor]) == current_height + 1:
                    to_visit.append(neighbor)
                    if neighbor_height == 9:
                        reachable_nines.add(neighbor)

    return len(reachable_nines)


def sol1(road_map: dict, starting_positions: list[complex]) -> int:
    total_score = 0
    for start_pos in starting_positions:
        score = bfs_trail_score(road_map, start_pos)
        total_score += score
    return total_score


if __name__ == '__main__':
    road_map, starting_positions = read_data("data.txt")
    score = sol1(road_map, starting_positions)
    print(score)
