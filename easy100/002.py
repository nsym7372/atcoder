import sys
n = int(input())
xl = list(map(int, input().split()))

mi = min(xl)
ma = max(xl)

ret = sys.maxsize
for i in range(mi, ma + 1):
    ret = min(ret,  sum([(_ - i) ** 2 for _ in xl]))

print(ret)