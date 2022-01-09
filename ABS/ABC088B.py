n = int(input())
al = list(map(int, input().split()))

alice = 0
bob = 0
for i, a in  enumerate(list(sorted(al, reverse=True))):
    if i % 2 == 0:
        alice += a
    else:
        bob += a

print(alice - bob)
