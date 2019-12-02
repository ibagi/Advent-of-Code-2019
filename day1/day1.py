import fileinput
import math

def calculate_fuel(mass):
   return math.floor(int(mass) / 3) - 2

solution = sum([calculate_fuel(mass) for mass in fileinput.input()])
print(solution)