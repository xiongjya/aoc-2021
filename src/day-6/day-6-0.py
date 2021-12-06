file = open("input/day-6-input.txt")
lines = file.readlines()[0]
fishes = [int(fish) for fish in lines.split(",")]
days = 0

new_fishes = []

while days < 80:
    for i, fish in enumerate(fishes):
        if fish == 0:
            new_fishes.append(8)
            fishes[i] = 6
        else:
            fishes[i] -= 1

    fishes.extend(new_fishes)
    new_fishes = []
    days += 1

print("fishes after 80 days: {}".format(len(fishes)))
