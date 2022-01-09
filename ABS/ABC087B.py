a_500 = int(input())
b_100 = int(input())
c_50 = int(input())
x = int(input())

cnt = 0
for a in range(a_500 + 1):
    for b in range(b_100 + 1):
        for c in range(c_50 + 1):
            if a * 500 + b * 100 + c * 50 == x:
                cnt += 1

print(cnt)