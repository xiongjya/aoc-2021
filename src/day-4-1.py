file = open('inputs/day-4-input.txt', 'r')
lines = file.readlines()

filtered = filter(lambda x: x != '\n', lines)   # filters out the new line separators for the input
lines = list(filtered)

numbers = lines[0].split(",")
lines = lines[1:]

puzzles = []
p = ""
count = 0

for line in lines:
    count += 1
    x = line.strip() + " "
    p += x

    if count == 5:
        puzzles.append(p.split())
        p = ""
        count = 0


def find(puzzle, number):   # checks if the number exists in the puzzle
    index = 0

    for ip in puzzle:
        if ip == number:
            puzzle[index] = "True"
            return True

        index += 1

    return False


def check(puzzle):
    bingo = True

    for r in range(0, 5):   # row check
        start = r * 5
        end = r * 5 + 5

        for number in puzzle[start:end]:
            if number != "True":
                bingo = False

        if bingo:
            return True
        else:
            bingo = True

    for c in range(0, 5):   # column check
        for i in range(0, 5):
            if puzzle[c + i * 5] != "True":
                bingo = False

        if bingo:
            return True
        else:
            bingo = True

    return False


def solve(puzzle, number):
    sum = 0

    for x in puzzle:
        if x != "True":
            sum += int(x)

    product = sum * int(number)
    print(product)


notSolved = list(range(0, len(puzzles)))
solved = False
index = 0

for n in numbers:
    if solved:
        break

    index = 0

    for p in puzzles:
        found = find(p, n)

        if found:
            bingo = check(p)

            if bingo and index in notSolved:
                notSolved.remove(index)

                if len(notSolved) == 0:
                    solve(p, n)
                    solved = True
                    break

        index += 1
