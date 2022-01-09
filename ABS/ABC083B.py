n, a, b = map(int, input().split())

s_sum = 0
for i in range(1, n + 1):
    sl = list(str(i))
    sm = sum([int(_) for _ in sl])
    if a <= sm <= b:
        s_sum += i
print(s_sum)