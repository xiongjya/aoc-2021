file = open("input/day-11-input.txt")
octopuses = [list(map(lambda i : int(i), list(line.strip()))) for line in file.readlines()]

step = 1
flashes = 0
to_flash = []
flashed = 0

# returns if there exists an octopus with energy level > 9
def scan() -> bool:
    b = False

    for r in range(0, 10):
        for c in range(0, 10):
            if octopuses[r][c] > 9:
                to_flash.append([r, c])
                b = True
    
    return b

def flash():
    for coord in to_flash:
        r = coord[0]
        c = coord[1]
        
        for row in range(-1, 2):
            for col in range(-1, 2):
                update(r + row, c + col)

        octopuses[r][c] = 0
        global flashed
        flashed += 1

def update(r, c):
    if r > -1 and r < 10 and c > -1 and c < 10:
        if octopuses[r][c] != 0:
            octopuses[r][c] += 1


while True:
    # increase each energy level by 1
    for r in range(0, 10):
        for c in range(0, 10):
            octopuses[r][c] += 1

    while scan():
        flashes += len(to_flash)
        flash()
        to_flash = []

    if flashed == 100:
        # print("all octopuses flashed: {}".format(step))   # part 2
        break

    flashed = 0
    step += 1


# print("flashes: {}".format(flashes))  # part 1: 1700