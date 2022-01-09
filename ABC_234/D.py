# tle

n, k = map(int, input().split())
pl = list(map(int, input().split()))

start = k
window = []
for l in range(start, n + 1):
    if l == start:
        window = list(sorted(pl[:l], reverse=True))
        print(window[k - 1])
    else:
        window.append(pl[l - 1])
        window.sort(reverse=True)
        print(window[k - 1])
        
        # for n in range(len(n_pl)):
        #     if n_pl[n] <= pl[l - 1]:
        #         n_pl.insert(n, pl[l - 1])
        #         break
        # else:
        #     n_pl.append(pl[l - 1])
    window.pop(k - 1)

