# put your python code here
import math

numbers = []

for _ in range(3):
    numbers.append(int(input()))

p = sum(numbers) / 2

S = math.sqrt(p * (p - numbers[0]) * (p - numbers[1]) * (p - numbers[2]))
print(S)
