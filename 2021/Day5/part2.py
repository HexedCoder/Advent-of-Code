def get_input():
    with open("input.txt") as input:
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


def check_segments(line_segments, planes):
    for line_segment in line_segments:
        start_x, start_y = line_segment[0].split(",")
        end_x, end_y = line_segment[1].split(",")
        start_x, start_y, end_x, end_y = int(start_x), int(start_y), int(
            end_x), int(end_y)

        planes[start_x][start_y] += 1
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

            planes[start_x][start_y] += 1

    return planes


def danger_spots(planes):
    bad_spots = 0
    for plane in planes:
        for num in plane:
            if num >= 2:
                bad_spots += 1
    print(bad_spots)


def main():
    line_segments = get_input()
    planes = build_plane()
    planes = check_segments(line_segments, planes)
    danger_spots(planes)


if __name__ == "__main__":
    main()