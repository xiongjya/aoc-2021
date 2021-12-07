import statistics

file = open("input/day-7-input.txt")
lines = file.readlines()[0]

crabs = [int(crab) for crab in lines.split(",")]
med = statistics.median(crabs)
fuel_consumption = int(sum(map(lambda crab : abs(crab - med), crabs)))

print("fuel consumption: {}".format(fuel_consumption))
