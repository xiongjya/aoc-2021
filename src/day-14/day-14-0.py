file = open("input/day-14-input.txt")
lines = [line.strip() for line in file.readlines()]
string = lines[0]

lines = list(map(lambda line : line.split(" -> "), lines[2:]))
template = {lines[i][0]: lines[i][1] for i in range(0, len(lines))}

step = 0
while step < 40:
    n = len(string)
    update = ""

    for i in range(0, n - 1):
        s = string[i:i+2]
        
        if s in template:
            x = string[i] + template[s]
            update += x
        else:
            update += string[i]

    update += string[-1]
    string = update

    step += 1

count = [0] * 26
for c in string:
    count[ord(c) - 65] += 1

count = list(filter(lambda n : n != 0, count))
difference = max(count) - min(count)

print("difference: {}".format(difference))
