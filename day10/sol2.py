from day10.sol1 import read_data


def count_paths(road_map, start_pos):
    steps = [1, -1, 1j, -1j]
    stack = [(start_pos, 0)]
    path_count = 0

    while stack:
        current_pos, current_height = stack.pop()

        if road_map[current_pos] == 9:
            path_count += 1
            continue

        for step in steps:
            neighbor = current_pos + step
            if neighbor in road_map and road_map[neighbor] == current_height + 1:
                stack.append((neighbor, road_map[neighbor]))

    return path_count


def sol2(road_map, starting_positions):
    total_score = 0
    for start_pos in starting_positions:
        total_score += count_paths(road_map, start_pos)
    return total_score


if __name__ == '__main__':
    road_map, starting_positions = read_data("data.txt")
    result = sol2(road_map, starting_positions)
    print("Total sum of trailhead scores:", result)
