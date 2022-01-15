n = int(input())
s_in = list(input())

result = 0
for i in range(n):
    if s_in[i:i + 3] ==  ["A", "B", "C"]:
        result += 1
print(result)

