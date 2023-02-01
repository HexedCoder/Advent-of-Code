def get_input():
    with open('input') as input:
        line_input = input.readlines()
    line_segments = []
    for line in line_input:
        line = line.split()
        line.pop(1)
        line_segments.append(line)

    return line_segments


def build_plane():
    new_plane = [0] * 1000
    planes = [new_plane.copy() for _ in range(0, 1000)]

    return planes


def check_segments_part_1(line_segments, planes1):
    for line_segment in line_segments:
        start_x, start_y = line_segment[0].split(",")
        end_x, end_y = line_segment[1].split(",")
        start_x, start_y, end_x, end_y = int(start_x), int(start_y), int(
            end_x), int(end_y)

        distance = max(abs(start_x - end_x), abs(start_y - end_y))
        for _ in range(0, distance + 1):
            if start_x == end_x:
                planes1[start_y][start_x] += 1
                if start_y < end_y:
                    start_y += 1
                elif start_y > end_y:
                    start_y -= 1

            elif start_y == end_y:
                planes1[start_y][start_x] += 1
                if start_x < end_x:
                    start_x += 1
                elif start_x > end_x:
                    start_x -= 1

    return planes1


def check_segments_part_2(line_segments, planes2):
    for line_segment in line_segments:
        start_x, start_y = line_segment[0].split(",")
        end_x, end_y = line_segment[1].split(",")
        start_x, start_y, end_x, end_y = int(start_x), int(start_y), int(
            end_x), int(end_y)

        planes2[start_x][start_y] += 1
        distance = max(abs(start_x - end_x), abs(start_y - end_y))

        for moves in range(0, distance):
            if start_x < end_x:
                start_x += 1
            elif start_x > end_x:
                start_x -= 1

            if start_y < end_y:
                start_y += 1
            elif start_y > end_y:
                start_y -= 1

            planes2[start_x][start_y] += 1

    return planes2


def danger_spots(planes):
    bad_spots = 0
    for plane in planes:
        for num in plane:
            if num >= 2:
                bad_spots += 1
    return bad_spots


def main():
    line_segments = get_input()
    planes1 = build_plane()
    planes2 = build_plane()
    planes1 = check_segments_part_1(line_segments, planes1)
    planes2 = check_segments_part_2(line_segments, planes2)

    print("Part 1:", danger_spots(planes1))
    print("Part 2:", danger_spots(planes2))


if __name__ == "__main__":
    main()
