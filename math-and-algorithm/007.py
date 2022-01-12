n, x, y = list(map(int, input().split()))

count = 0
for _ in range(1, n + 1):
    if _ % x == 0 or _ % y == 0:
        count += 1
print(count)