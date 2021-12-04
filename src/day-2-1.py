file = open('inputs/day-2-input.txt', 'r')
lines = file.readlines()

aim = 0
breadth = 0
depth = 0

for line in lines:
    directions = line.split()
    dir = directions[0]
    n = int(directions[1])

    if dir == 'forward':
        breadth += n
        m = aim * n
        depth += m
    elif dir == 'up':
        aim -= n
    elif dir == 'down':
        aim += n

area = breadth * depth

print("result: {}".format(area))