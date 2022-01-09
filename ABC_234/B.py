import math
n = int(input())

x_in = []
y_in = []
for _ in range(n):
    x, y = map(int, input().split())
    x_in.append(x)
    y_in.append(y)

dis = 0
for i in range(0, n):
    for j in range(i + 1, n):
        tmp = float(format( math.sqrt((x_in[i] - x_in[j]) ** 2 + (y_in[i] - y_in[j]) ** 2), ".8f"))
        dis = max(dis, tmp)

print(dis)
