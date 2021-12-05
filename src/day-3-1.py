file = open('inputs/day-3-input.txt', 'r')
lines = file.readlines()

first = lines[0]
n = len(first) - 1  # number of bits in each line

onum = 0    # number of lines in the oxygen list
cnum = 0    # number of lines in carbon dioxide list

ocount = [0] * n    # keeps track of the number of 1s in each index for oxygen
ccount = [0] * n    # keeps track of the number of 1s in each index for carbon dioxide

olst = lines
clst = lines


def narrow_down(index, counter, lst, arr, is_oxygen):
    if len(lst) == 1:
        return lst

    for element in lst:
        counter += 1
        x = int(element[index])

        if x == 1:
            arr[index] += 1

    half = counter / 2

    if arr[index] >= half:
        arr[index] = is_oxygen
    else:
        arr[index] = (1 - is_oxygen)

    filtered = filter(lambda y: int(y[index]) == arr[index], lst)

    return list(filtered)


for i in range(0, n):
    onum = 0
    cnum = 0

    olst = narrow_down(i, onum, olst, ocount, 1)
    clst = narrow_down(i, cnum, clst, ccount, 0)

oxygen = int(olst[0], 2)
carbon = int(clst[0], 2)

life_support = oxygen * carbon

print("oxygen: {}".format(oxygen))
print("carbon: {}".format(carbon))
print("life support rating: {}".format(life_support))
