import sys
n, y = map(int, input().split())

for i in range(0, n + 1):
    for j in range(i, n + 1):
        for k in range(j, n + 1):
            if i * 10000 + j * 5000 + k * 1000 == y:
                print(f"{i} {j} {k}")
                sys.exit()
print(-1, -1, -1)