import sys
n = int(input())

in_l = []
for _ in range(n):
    in_l.append(list(map(int, input().split())))
in_l.insert(0, [0, 0, 0])

for i in range(n):
    l_now = in_l[i]
    l_next = in_l[i + 1]


    dt = l_next[0] - l_now[0]
    dx = abs(abs(l_next[1]) - abs(l_now[1]))
    dy = abs(abs(l_next[2]) - abs(l_now[2]))
    
    # print(f"dx: {dx} / dy: {dy}")

    if (dt - (dx + dy)) % 2 != 0 or dt < (dx + dy) :
        print("No")
        sys.exit()
print("Yes")
    