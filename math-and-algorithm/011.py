n = int(input())

result = []
for i in range(2, n + 1):
    if i == 2 or i == 3 or i == n + 1:
        result.append(i)
        continue

    for j in range(2, i):
        if i % j == 0:
            break
    else:
        result.append(i)
print(*result)