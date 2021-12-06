file = open("input/day-6-input.txt")
lines = file.readlines()[0]

fishes = [int(fish) for fish in lines.split(",")]
fish_count = [0] * 9

for fish in fishes:
    fish_count[fish] += 1

days = 0
while days < 256:
    new = fish_count.pop(0)
    fish_count[6] += new
    fish_count.append(new)

    days += 1

print("fishes after 256 days: {}".format(sum(fish_count)))
