import math

number = int(input())

function = math.exp(number) / (math.exp(number) + 1)

print(round(function, 2))

