file = open('inputs/day-2-input.txt', 'r')
lines = file.readlines()

breadth = 0
depth = 0

for line in lines:
    directions = line.split()
    dir = directions[0]
    n = int(directions[1])

    if dir == 'forward':
        breadth += n
    elif dir == 'up':
        depth -= n
    elif dir == 'down':
        depth += n

area = breadth * depth

print("result: {}".format(area))