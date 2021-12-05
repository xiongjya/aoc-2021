file = open('input/day-5-input.txt', 'r')
lines = file.readlines()

x_max = 0   # maximum x-coordinate / row
y_max = 0   # maximum y-coordinate / column
coords = []


def mark_straight(is_vertical, constant, n, m, map):
    start = min(n, m)
    end = max(n, m)

    for i in range(start, end + 1):
        if is_vertical:
            map[i][constant] += 1
        else:
            map[constant][i] += 1


for line in lines:
    coord = line.split(" -> ")
    coord[0] = coord[0].split(",")
    coord[1] = coord[1].split(",")

    if int(coord[0][0]) == int(coord[1][0]) or int(coord[0][1]) == int(coord[1][1]):
        coords.append(coord)

    x_max = max(max(int(coord[0][0]), int(coord[1][0])), x_max)
    y_max = max(max(int(coord[0][1]), int(coord[1][1])), y_max)

x_max += 1
y_max += 1
map = [0] * y_max

for i in range(0, y_max):
    map[i] = [0] * x_max

for coord in coords:
    is_vertical = int(coord[0][0]) - int(coord[1][0]) == 0

    if is_vertical:
        mark_straight(is_vertical, int(coord[0][0]), int(coord[0][1]), int(coord[1][1]), map)
    else:
        mark_straight(is_vertical, int(coord[0][1]), int(coord[0][0]), int(coord[1][0]), map)

result = 0
for r in range(0, y_max):
    for c in range(0, x_max):
        if (map[r][c] > 1):
            result += 1

print("result: {}".format(result))
