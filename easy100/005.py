n, m, c = map(int, input().split())
bl = list(map(int, input().split()))

def is_success(al):
    value = 0
    for a, b in zip(al, bl):
        value += a * b
    value += c
    return value > 0

result = 0
for _ in range(n):
    al = list(map(int, input().split()))
    result += 1 if is_success(al) else 0

print(result)