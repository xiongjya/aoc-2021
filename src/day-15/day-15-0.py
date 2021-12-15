file = open("input/day-15-input.txt")
caverns = [list(map(lambda s : int(s), list(line.strip()))) for line in file.readlines()]

class Cave:
    def __init__(self, r, c, value):
        self.r = r
        self.c = c
        self.value = value
        self.visited = False

rows = len(caverns)
cols = len(caverns[0])

for i in range(0, rows):
    for j in range(0, cols):
        caverns[i][j] = Cave(i, j, caverns[i][j])

to_visit = [caverns[0][0]]

while len(to_visit) > 0:
    cave = to_visit.pop(0)
    r = cave.r
    c = cave.c
    cave.visited = True
    next = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
    
    for coord in next:
        if coord[0] >= 0 and coord[0] < rows and coord[1] >= 0 and coord[1] < cols:
            cv = caverns[coord[0]][coord[1]]
            if cv not in to_visit and not cv.visited:
                cv.value += cave.value
                to_visit.append(cv)

    to_visit.sort(key=lambda c : c.value)

print("lowest total risk: {}".format(caverns[rows - 1][cols - 1].value - caverns[0][0].value))