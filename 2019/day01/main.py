import math


def get_fuel(mass):
    return math.floor(mass / 3) - 2


def get_fuel_recursive(mass, total=0):
    fuel = get_fuel(mass)
    if fuel <= 0:
        return total
    return get_fuel_recursive(fuel, total + fuel)


with open("input.txt") as f:
    masses = [int(line.strip()) for line in f.readlines()]

fuels = [get_fuel_recursive(mass) for mass in masses]
total_fuel = int(sum(fuels))
print("total fuel: ", total_fuel)
