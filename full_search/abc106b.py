n = int(input())

if n < 105:
    print(0)
    exit()

result = 0
for i in range(105, n + 1, 2):
    divisor = 0
    for j in range(1, n + 1):
        if i % j == 0:
            divisor += 1
    
    if divisor == 8:
        result += 1
print(result)