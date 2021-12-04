file = open('inputs/day-3-input.txt', 'r')
lines = file.readlines()

first = lines[0]
n = len(first) - 1  # number of bits in each line
i = 0   # number of lines in the input file

count = [0] * n # keeps track of the number of 1s in each index

for line in lines:
    i += 1

    for j in range(0, n):
        x = int(line[j])

        if x == 1:
            count[j] += 1

half = i / 2
max = 2 ** n - 1
gamma = 0
epsilon = 0

for j in range(n - 1, -1, -1):
    x = count[(n - 1) - j]

    if x >= half:
        gamma += 2 ** j

epsilon = max - gamma
power = gamma * epsilon

print("gamma: {}".format(gamma))
print("epsilon: {}".format(epsilon))
print("power: {}".format(power))