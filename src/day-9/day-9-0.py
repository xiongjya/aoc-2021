import bisect

file = open("input/day-9-input.txt")
caves = [list(map(lambda s : int(s), list(line.strip()))) for line in file.readlines()]

rows = len(caves) - 1
cols = len(caves[0]) - 1

low_points = []
visited = []
basins = []

def get(r, c) -> int:
    if r < 0 or r > rows or c < 0 or c > cols:
        return 10
    else:
        return caves[r][c]

def is_low_point(r, c) -> bool:
    n = caves[r][c]
    neighbours = [get(r, c + 1), get(r, c - 1), get(r + 1, c), get(r - 1, c)]

    return all(map(lambda neighbour : neighbour > n, neighbours))

def find_basin(r, c) -> int:
    if r < 0 or r > rows or c < 0 or c > cols:  # invalid coordinates
        return 0
    elif caves[r][c] == 9:  # stop expanding frontier
        return 0
    elif visited[r][c]: # visited
        return 0
    else:
        visited[r][c] = True
        return 1 + find_basin(r, c + 1) + find_basin(r, c - 1) + find_basin(r + 1, c) + find_basin(r - 1, c)

for r in range(0, rows + 1):
    visited.append([False] * (cols + 1))
    
for r in range(0, rows + 1):
    for c in range(0, cols + 1):
        if is_low_point(r, c):
            # low_points.append(caves[r][c])    # part 1
            size = find_basin(r, c)   # part 2
            
            bisect.insort(basins, size)

            if len(basins) > 3:
                basins.pop(0)

# result = sum(map(lambda n : n + 1, low_points))   # part 1
# print("number of low points: {}".format(result))

result = basins[0] * basins[1] * basins[2]
print("product of largest basin sizes: {}".format(result))
