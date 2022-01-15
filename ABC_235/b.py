n = input()
hl = list(map(int, input().split()))

result = 0
for h in hl:
    if h <= result:
        print(result)
        exit()
    result = max(h, result)

print(result)