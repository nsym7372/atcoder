import sys
s =  "".join(reversed(input()))

words =  list( ["".join(_) for _ in map(reversed, ["dreamer", "eraser", "dream", "erase"])])

while(len(s) != 0):
    for word in words:
        if s.startswith(word):
            s = s[len(word):]
            break
    else:
        print("NO")
        sys.exit()
        
print("YES")