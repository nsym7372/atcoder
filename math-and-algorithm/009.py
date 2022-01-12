n, s = map(int, input().split())
al = list(map(int, input().split()))

ns = "i" * n

for i in range(2 ** n):
    pattern = format(i, f"0{n}b")

    result = 0
    for a, p in zip(al, pattern):
        result += a if p == "1" else 0
        if result == s:
            print('Yes')
            exit()

print('No')
