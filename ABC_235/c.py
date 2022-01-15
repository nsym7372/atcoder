n, iq = map(int, input().split())
al = list(map(int, input().split()))
ql = []
for i in range(iq):
    ql.append(list(map(int, input().split())))

m = {}
for i, a in enumerate(al):
    if a not in m.keys():
        m[a] = []
    m[a].append(i + 1)

for q in ql:
    if q[0] not in m.keys():
        print(-1)
        continue
    l = m[q[0]]
    print(l[q[1] - 1] if q[1] - 1 < len(l) else -1)


# tle
# for q in ql:
#     ml = [i for i, j in enumerate(al) if j == q[0]]
#     print(ml[q[1] - 1] + 1 if q[1] <= len(ml) else -1)


# tle
# for q in ql:
#     idx = 0
#     cnt = 0
#     for i in range(n):
#         if q[0] == al[i]:
#             idx = i
#             cnt += 1
        
#         if cnt == q[1]:
#             print(idx + 1)
#             break
#     else:
#         print(-1)

