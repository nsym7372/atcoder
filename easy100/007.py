card = []
bingo = [
    [False, False, False],
    [False, False, False],
    [False, False, False],
]

def call(b):
    for r in range(len(card)):
        for c in range(len(card[0])):
            if card[r][c] == b:
                bingo[r][c] = True

def is_bingo():
    is_row_bingo()
    is_col_bingo()
    is_cross_bingo()

def is_row_bingo():
    for r in bingo:
        if all(_ for _ in r):
            print("Yes")
            exit()

def is_col_bingo():
    for c in range(len(bingo[0])):
        result = True
        for r in range(len(bingo)):
            if bingo[r][c] != True:
                result = False
        if result:
            print("Yes")
            exit()

def is_cross_bingo():
    if bingo[0][0] and bingo[1][1] and bingo[2][2]:
        print("Yes")
        exit()

    if bingo[0][2] and bingo[1][1] and bingo[2][0]:
        print("Yes")
        exit()


for i in range(3):
    card.append(list(map(int, input().split())))

n = int(input())

for j in range(n):
    call(int(input()))

is_bingo()

print("No")



