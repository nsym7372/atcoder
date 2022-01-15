s_in = list(input())
acgt = list("ACGT")

def is_acgt(word):
    for a in acgt:
        if word == a:
            return True
    return False

result = 0
now = 0
for i in range(len(s_in)):
    if is_acgt(s_in[i]):
        now += 1
        result = max(result, now)
    else:
        now = 0

print(result)
