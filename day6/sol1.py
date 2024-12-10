"""
If there is something directly in front of you, turn right **90 degrees**.
Otherwise, take a step forward.
"""
import typing


def read_input(filename) -> dict:
    global SIZE, LOCATION
    _map = {}
    with open(filename) as file:
        data = file.read().split("\n")
        SIZE = len(data)
        for row_i, line in enumerate(data):
            for char_i, char in enumerate(line):
                _map[complex(row_i, char_i)] = char
                if char == "^":
                    LOCATION = complex(row_i, char_i)
    return _map


def sol1(_map: dict, _location: complex, _size: int, step: typing.Optional[complex] = -1) -> int:
    visited, directions = set(), {-1: 1j, 1j: 1, 1: -1j, -1j: -1}
    while True:
        visited.add(_location)
        next_char = _map.get(_location + step, None)
        if next_char is None:
            break
        elif next_char == "#":
            step = directions[step]
        _location += step
    return len(visited)


if __name__ == "__main__":
    LOCATION = complex(0, 0)
    SIZE = 0
    MAP = read_input("data.txt")
    sol1(MAP, LOCATION, SIZE)
