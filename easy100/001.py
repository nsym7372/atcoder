a, b = map(int, input().split())

result = 0
while(True):
    if ((a - 1) * result + 1 >= b):
        print(result)
        exit()
    result += 1