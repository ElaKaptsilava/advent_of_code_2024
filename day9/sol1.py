def read_data(file_name):
    with open(file_name) as file:
        data = list(file.read())
    data = list(map(int, data))
    return data


def generate_disk_representation(parsed_map):
    """Generates a detailed disk representation from parsed map."""
    disk = []
    file_id = 0
    for i, length in enumerate(parsed_map):
        if i % 2 == 0:
            disk.extend([str(file_id)] * length)
            file_id += 1
        else:
            disk.extend(['.'] * length)
    return disk


def compress_disk(disk):
    """Compress the disk by moving file blocks left into free spaces."""
    point = "."

    left_pos = 0
    right_pos = len(disk) - 1
    while True:
        if len(set(disk[left_pos:])) == 1:
            break
        if left_pos == right_pos:
            right_pos = len(disk) - 1
        left_file = disk[left_pos]
        right_file = disk[right_pos]
        if left_file == point:
            while right_file == point:
                right_pos -= 1
                right_file = disk[right_pos]
            disk[left_pos], disk[right_pos] = right_file, point
        left_pos += 1

    return ''.join(disk)


def calculate_checksum(compressed_disk):
    """Calculates the checksum of the compressed disk."""
    checksum = 0
    for position, block in enumerate(compressed_disk):
        if block != '.':
            checksum += position * int(block)
    return checksum


if __name__ == "__main__":
    data = read_data("data.txt")
    # parsed_map = parse_disk_map(data)
    disk = generate_disk_representation(data)
    compressed_disk = compress_disk(disk)
    checksum = calculate_checksum(compressed_disk)
    print("".join(compressed_disk))
    # print("0099811188827773336446555566")
    print(checksum)
    # too low 114202686405, 114204650151,
    # not correct 85906678741
    # correct 6399153661894
