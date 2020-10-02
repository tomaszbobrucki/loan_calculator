import math

a = int(input())
b = int(input())

if b < 2:
    print(round(math.log(a), 2))
else:
    print(round(math.log(a, b), 2))
