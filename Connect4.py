l = 8
h = 6
board =[]
valid = []

def p(a):
    for i in range(h):
        print(board[h-1-i])
def findy(a):
    for i in range(l):
        if board[i][a] == '⬛':
            return i
def check (a, z):
    # horizontalCheck 
    for j in range (l-3):
        for i in range (h):
            if a[i][j] == z and a[i][j+1] == z and a[i][j+2] == z and a[i][j+3] == z:
                return True;              
    # verticalCheck
    for i in range (h-3):
        for j in range(l):
            if (a[i][j] == z and a[i+1][j] == z and a[i+2][j] == z and a[i+3][j] == z):
                return True;        
    # ascendingDiagonalCheck 
    for i in range (3,h):
        for j in range(l-3):
            if a[i][j] == z and a[i-1][j+1] == z and a[i-2][j+2] == z and a[i-3][j+3] == z:
                return True;
    # descendingDiagonalCheck
    for i in range(3,h):
        for j in range(3,l):
            if a[i][j] == z and a[i-1][j-1] == z and a[i-2][j-2] == z and a[i-3][j-3] == z:
                return True;
    
    return False;

for i in range(l):
    board .append(['⬛']*l)
    valid.append(str(i+1))
players = ['🟥', '🟨']
turn =0
print (valid)
while 1:
    p(board)
    selection = input()
    if (selection in valid):
        token = players[turn % len(players)]
        turn +=1
        yVal = findy (int(selection) - 1)
        if yVal == h-1: valid.remove(selection)
        board [yVal][int(selection) - 1] = token
        if check(board, token):
            p(board)
            print(token +" Wins")
            break;
        if len (valid) == 0: 
            p(board)
            print("Tie")
            break
