import sys
n, y = map(int, input().split())

for i in range(0, n + 1):
    for j in range(0, n + 1):
        k = n - i - j
        # print(f"i: {i} / j: {j} / k: {k}")
        if k < 0 or i * 10000 + j * 5000 + k * 1000 != y:
            continue
        else:
            print(f"{i} {j} {k}")
            sys.exit()

print(-1, -1, -1)