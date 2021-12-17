file = open("input/day-17-input.txt")
lines = file.readlines()[0].strip()

trench_y = lines.find("y")
trench_x = list(map(lambda n : int(n), lines[15:trench_y - 2].split("..")))
trench_y = list(map(lambda n : int(n) ,lines[trench_y + 2:].split("..")))

max_ys = []

for x in range(1, trench_x[1] + 1):
    for y in range(-1000, 1000):
        x_change, y_change = x, y
        x_pos, y_pos = 0, 0
        y_max = 0
        while x_pos <= trench_x[1] and y_pos >= trench_y[0]:
            x_pos += x_change
            y_pos += y_change
            x_change = x_change - 1 if x_change > 0 else 0
            y_change -= 1
            y_max = max(y_pos, y_max)

            if trench_x[0] <= x_pos <= trench_x[1] and trench_y[0] <= y_pos <= trench_y[1]:
                max_ys.append(y_max)
                break

result = max(max_ys)
print("highest y position: {}".format(result))  # part 1
print("number of initial velocities: {}".format(len(max_ys)))   # part 2
