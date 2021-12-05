file = open('input/day-1-input.txt', 'r')
lines = file.readlines()

first = True
previous = 0
count = 0

for line in lines:
    x = int(line)

    if first:
        previous = x
        first = False
    elif x > previous:
        count += 1

    previous = x

print("result: {}".format(count))