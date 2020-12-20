import queue
board = [
['x','s','x','o','o','o','x','o'],
['o','o','x','o','o','x','o','o'],
['o','x','x','o','x','x','o','x'],
['o','x','x','o','o','x','o','x'],
['o','x','x','x','o','x','o','x'],
['o','o','x','x','o','x','o','o'],
['x','o','o','o','o','o','x','o'],
['x','e','x','x','x','o','o','o']
]
# def isValid(board,positions):
#     if(positions[0]>=len(board) or positions[0]<0 or positions[1]>= len(board) or positions[1]<0):
#         return False
#     if(board[positions[0]][positions[1]] == 'x'):
#         return False
#     return True
# def isEnd(board, positions):
#     if(board[positions[0]][positions[1]] == 'e'):
#         return True
#     return False
# q = queue.Queue()
# q.put((0,1))
# visited = set()
# while(not q.empty()):
#     curr = q.get()
#     if(isEnd(board,curr)):
#         print("Found End")
#         print(curr)
#         break
#     if(isValid(board,(curr[0],curr[1]+1))):
#         q.put((curr[0],curr[1]+1))
#         visited.add((curr[0],curr[1]+1))
#     if(isValid(board,(curr[0],curr[1]-1))):
#         q.put((curr[0],curr[1]-1))
#         visited.add((curr[0],curr[1]-1))
#     if(isValid(board,(curr[0]+1,curr[1]))):
#         q.put((curr[0]+1,curr[1]))
#         visited.add((curr[0]+1,curr[1]))
#     if(isValid(board,(curr[0]-1,curr[1]))):
#         q.put((curr[0]-1,curr[1]))
#         visited.add((curr[0]-1,curr[1]))
# for i in visited:
#     if board[i[0]][i[1]] == 'o':
#         board[i[0]][i[1]] = 'v'
# for i in board:
#     print(i)

    
# def createMaze2():
#     maze = []
#     maze.append(["x","s", "x", "o", "o", "o", "x", "#e"])
#     maze.append(["o","o", "x", "o", "o", "x", "o", "o"])
#     maze.append(["o","x", "x", "o", "x", "x", "o", "x"])
#     maze.append(["o","x", "x", "o", "o", "x", "o", "x"])
#     maze.append(["o","x", "x", "x", "#", "o", "#", " ", "#"])
#     maze.append(["o","o", "x", "x", "#", "o", "#", " ", "#"])
#     maze.append(["x","o", "o", "o", "#", "o", "#", "#", "#"])
#     maze.append(["o","o", "x", "x", " ", "x", " ", " ", "#"])

#     return maze
def valid(maze, moves):
    i = 0
    j = 0
    for x, row in enumerate(maze):
        for y,col in enumerate(row):
            if col =='s':
                i = x
                j = y
    for move in moves:
        if move == "L":
            j -= 1

        elif move == "R":
            j += 1

        elif move == "U":
            i -= 1

        elif move == "D":
            i += 1

        if not(0 <= j < len(maze[0]) and 0 <= i < len(maze)):
            return False
        elif (maze[i][j] == "x"):
            return False
        if(maze[i][j] != 's' and maze[i][j] != 'e'):
            maze[i][j] = 'v'
    return True

def printMaze(maze, path=""):
    i = 0
    j = 0
    for x, row in enumerate(maze):
        for y,col in enumerate(row):
            if col =='s':
                i = x
                j = y

    pos = set()
    for move in path:
        if move == "L":
            j -= 1

        elif move == "R":
            j += 1

        elif move == "U":
            i -= 1

        elif move == "D":
            i += 1
        pos.add((i, j))
    
    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            if (i, j) in pos:
                print("+ ", end="")
                if(col != 'e'):
                    maze[i][j] = '+'
            else:
                print(col + " ", end="")
        print()

def findEnd(maze, moves):
    i = 0
    j = 0
    for x, row in enumerate(maze):
        for y,col in enumerate(row):
            if col =='s':
                i = x
                j = y
    for move in moves:
        if move == "L":
            j -= 1

        elif move == "R":
            j += 1

        elif move == "U":
            i -= 1

        elif move == "D":
            i += 1

    if maze[i][j] == "e":
        print("Found: " + moves)
        printMaze(maze,moves)
        return True

    return False


# MAIN ALGORITHM

nums = queue.Queue()
nums.put("")
add = ""
maze = board

while not findEnd(board, add): 
    add = nums.get()
    #print(add)
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(board, put):
            nums.put(put)
for i in maze:
    print(i)