file = open("input/day-13-input.txt")
lines = map(lambda l : l.strip(), filter(lambda l : not l.isspace(), file.readlines()))
dots = []
instructions = []

for line in lines:
    if line[0] == "f":
        instructions.append(line[11:].split("="))
        # break     # for part 1
    else:
        coords = list(map(lambda n : int(n), line.split(",")))
        dots.append(coords)

for instruction in instructions:
    updated = []
    for dot in dots:
        p = int(instruction[1])
        coord = dot[0] if instruction[0] == "x" else dot[1]
        if coord < p:
            updated.append(dot)
        elif coord > p:
            difference = coord - p
            if instruction[0] == "x":
                if [p - difference, dot[1]] not in dots:
                    updated.append([p - difference, dot[1]])
            else:
                if [dot[0], p - difference] not in dots:
                    updated.append([dot[0], p - difference])
            
    dots = updated

max_x = max(map(lambda d : d[0], dots))
max_y = max(map(lambda d : d[1], dots))
result = []

for x in range(0, max_y + 1):
    result.append([" "] * (max_x + 1))

for d in dots:
    result[d[1]][d[0]] = "#"

for row in result:
    print("".join(row))

# print("number of dots visible after first fold: {}".format(len(dots)))    # part 1
