import sys

file = open("input/day-7-input.txt")
lines = file.readlines()[0]

crabs = [int(crab) for crab in lines.split(",")]
fuel_consumption = sys.maxsize

def arithmetic_series(difference):
    return int(difference * (difference + 1) / 2)

for r in range(min(crabs), max(crabs) + 1):
    i = sum(map(lambda crab : arithmetic_series(abs(crab - r)), crabs))
    fuel_consumption = min(i, fuel_consumption)

print("fuel consumption: {}".format(fuel_consumption))
