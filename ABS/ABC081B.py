n = int(input())
al = list(map(int, input().split()))

cnt = 0
con = True
while con:
    for j in range(len(al)):
        if al[j] % 2 != 0:
            con = False
            break
        al[j] = al[j] / 2

    else:
        cnt += 1

print(cnt)