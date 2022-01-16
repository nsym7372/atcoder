n, a, b = map(int, input().split())
sl = list(input())

now = 0
over_sea = 0

def success(s):
    global over_sea
    global now
    if s == "a" and now < a + b:
        now += 1
        return True
    elif s == "b" and now < a + b and over_sea < b:
        now += 1
        over_sea += 1
        return True
    else:
        return False

for _ in sl:
    print("Yes" if success(_) else "No")
