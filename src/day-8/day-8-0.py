file = open("input/day-8-input.txt")
lines = file.readlines()
output = [line.strip().split(" | ")[1] for line in lines]

def length(str) -> bool:
    n = len(str)
    return (n > 1 and n < 5) or n == 7

result = sum(map(lambda ls : len(list(filter(lambda element : length(element), ls.split(" ")))), output))

print("result: {}".format(result))
