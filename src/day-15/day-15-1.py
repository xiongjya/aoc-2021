file = open("input/day-15-input.txt")
lines = [list(map(lambda s : int(s), list(line.strip()))) for line in file.readlines()]

class Cave:
    def __init__(self, r, c, value):
        self.r = r
        self.c = c
        self.value = value
        self.visited = False

rows = len(lines)
cols = len(lines[0])
max_rows = rows * 5
max_cols = cols * 5
caverns = []

for i in range(0, max_rows):
    caverns.append([None] * max_cols)
    for j in range(0, max_cols):
        if i < rows and j < cols:
            caverns[i][j] = Cave(i, j, lines[i][j])
        else:
            x = int(i / rows)
            y = int(j / cols)
            difference = x + y
            x = i - x * rows
            y = j - y * cols
            v = difference + lines[x][y]
            if v > 9:
                v -= 9
            caverns[i][j] = Cave(i, j, v)

to_visit = [caverns[0][0]]

while len(to_visit) > 0:
    cave = to_visit.pop(0)
    r = cave.r
    c = cave.c
    cave.visited = True
    next = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
    
    for coord in next:
        if coord[0] >= 0 and coord[0] < max_rows and coord[1] >= 0 and coord[1] < max_cols:
            cv = caverns[coord[0]][coord[1]]
            if cv not in to_visit and not cv.visited:
                cv.value += cave.value
                to_visit.append(cv)

    to_visit.sort(key=lambda c : c.value)

print("lowest total risk: {}".format(caverns[max_rows - 1][max_cols - 1].value - caverns[0][0].value))