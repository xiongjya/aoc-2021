file = open('inputs/day-1-input.txt', 'r')
lines = file.readlines()

set = [0, 0, 0]
count = 0
result = 0

for line in lines:
    x = int(line)

    if count < 3:
        set[count] = x
        count += 1
        continue

    if count % 3 == 0:
        if x > set[0]:
            result += 1
        set[0] = x
    elif count % 3 == 1:
        if x > set[1]:
            result += 1
        set[1] = x
    elif count % 3 == 2:
        if x > set[2]:
            result += 1
        set[2] = x

    count += 1

print("result: {}".format(result))