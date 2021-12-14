file = open("input/day-14-input.txt")
lines = [line.strip() for line in file.readlines()]
string = lines[0]

lines = list(map(lambda line : line.split(" -> "), lines[2:]))
template = {lines[i][0]: lines[i][1] for i in range(0, len(lines))}
pattern_count = {key: 0 for key in template}
letter_count = [0] * 26

for i in range(0, len(string) - 1):     # initialisation
    s = string[i:i+2]
    if s in pattern_count:
        pattern_count[s] += 1

for c in string:
    letter_count[ord(c) - 65] += 1

step = 0
while step < 40:
    updated_pattern = {key: 0 for key in template}

    for key in pattern_count:
        if pattern_count[key] != 0:
            to_add = template[key]  # new character to insert
            x = key[0] + to_add     # new string pattern one
            y = to_add + key[1]     # new string pattern two

            if x in template:   # if is a valid pattern, update
                updated_pattern[x] += pattern_count[key]

            if y in template:   # if is a valid pattern, update
                updated_pattern[y] += pattern_count[key]

            letter_count[ord(to_add) - 65] += pattern_count[key]

    pattern_count = updated_pattern
    step += 1

letter_count = list(filter(lambda n : n != 0, letter_count))
difference = max(letter_count) - min(letter_count)
print("difference: {}".format(difference))
