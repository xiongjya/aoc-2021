file = open("input/day-8-input.txt")
lines = [line.strip() for line in file.readlines()]

numbers = {}

def sort(str):
    return "".join(sorted(str))

def verify_known_numbers(arr):
    for s in arr:
        if len(s) == 2:
            numbers[sort(s)] = 1
        elif len(s) == 3:
            numbers[sort(s)] = 7
        elif len(s) == 4:
            numbers[sort(s)] = 4
        elif len(s) == 7:
            numbers[sort(s)] = 8

def find_six(input):
    one = list(filter(lambda s : len(s) == 2, input))[0]
    six = list(filter(lambda s : not all(map(lambda x : x in s, one)), filter(lambda s : len(s) == 6, input)))[0]
    numbers[sort(six)] = 6

def find_nine(input):
    four = list(filter(lambda s : len(s) == 4, input))[0]
    nine = list(filter(lambda s : all(map(lambda x : x in s, four)), filter(lambda s : len(s) == 6, input)))[0]
    numbers[sort(nine)] = 9

    return nine

def find_zero(input):
    zero = list(filter(lambda s : len(s) == 6 and sort(s) not in numbers, input))[0]
    numbers[sort(zero)] = 0

def find_three(input):
    one = list(filter(lambda s : len(s) == 2, input))[0]
    three = list(filter(lambda s : all(map(lambda x : x in s, one)), filter(lambda s : len(s) == 5, input)))[0]
    numbers[sort(three)] = 3

def find_five(input, nine):
    one = list(filter(lambda s : len(s) == 2, input))[0]
    five = list(filter(lambda s : not all(map(lambda x : x in s, one)) and all(map(lambda x : x in nine, s)), filter(lambda s : len(s) == 5, input)))[0]
    numbers[sort(five)] = 5

def find_two(input):
    two = list(filter(lambda s : len(s) == 5 and sort(s) not in numbers, input))[0]
    numbers[sort(two)] = 2

def generate(arr) -> int:
    result = 0
    for i, n in enumerate(arr):
        result += n* 10**(3 - i)

    return result

def solve(str) -> int:
    global numbers
    numbers = {}

    arr = str.split(" | ")
    input = arr[0].split()
    output = arr[1].split()

    verify_known_numbers(input)
    find_six(input)
    nine = find_nine(input)
    find_zero(input)
    find_three(input)
    find_five(input, nine)
    find_two(input)

    return generate(map(lambda s : numbers[sort(s)], output))

result = sum(map(lambda line : solve(line), lines))
print("result: {}".format(result))
