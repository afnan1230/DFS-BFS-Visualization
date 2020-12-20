import time
board = [
['x','s','x','o','o','o','x','e'],
['o','o','x','o','o','x','o','o'],
['o','x','x','o','x','x','o','x'],
['o','x','x','o','o','x','o','x'],
['o','x','x','x','o','x','o','x'],
['o','o','x','x','o','x','o','o'],
['x','o','o','o','o','o','x','o'],
['o','o','x','x','x','o','o','o']
]
def ExitMaze(board, xpos, ypos):
    if(xpos<0 or xpos>= 8 or ypos<0 or ypos>= 8):
        return 0
    if(board[xpos][ypos] == 'e'):
        return 1
    if(board[xpos][ypos] == 'v' or board[xpos][ypos] == 'x'):
        return 0
    board[xpos][ypos] = 'v'
    for i in board:
        print(i)
    print()
    if(ExitMaze(board,xpos+1,ypos)):
        board[xpos][ypos] = 'p'
        return 1
    
    if(ExitMaze(board,xpos, ypos+1)):
        board[xpos][ypos] = 'p'
        return 1
    if(ExitMaze(board,xpos-1, ypos)):
        board[xpos][ypos] = 'p'
        return 1
    if(ExitMaze(board,xpos, ypos-1)):
        board[xpos][ypos] = 'p'
        return 1
    return 0
ExitMaze(board,0,1)
# time.sleep(10)

for i in board:
    print(i)



