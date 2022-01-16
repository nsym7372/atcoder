import math
n = int(input())

s = math.ceil(n / 1.08)
d = math.floor(s * 1.08)

print(s if n == d else ":(")