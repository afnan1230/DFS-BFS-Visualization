"""
Visualization.py

Author: Afnan Mir
Created: 12/17/2020
Last Modfied: 12/18/2020
Description: Provide a visualization of a Breadth First Search and a Depth First Search
on a maze to solve it
"""
import pygame
import time
import constants
import sys
import time
import queue
pygame.font.init()
black = (0,0,0)
white = (255,255,255)
gray = (150,150,150)
red = (255,0,0)
green = (0,255,0)
yellow = (255,255,0)

#class for the buttons to be pressed
class button():
    """
    Button class to set up buttons for Breadth First Search and Depth First Search Options
    """
    def __init__(self, color, x,y,width,height, text=''):
        """
        init
        Args:
            - color: color of the button
            -x: the x position of top left corner of the button
            -y: the y position of the top left corner of the button
            -width: width of the button
            -height: height of the button
            -text: text inside the button
        Returns:
            -None
        """
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        """
        draws the button
        Args:
            -win: the window that the button goes on
            -outline: whether or not the button will have an outline or not
        """
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 30)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        """
        checks to see if position of the mouse is over the button

        Args:
            -pos: the position of the mouse
        Return
            -Whether the position of the mouse is over the button
        """
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

class Game():
    """
    create main framework for the game, grid, and event handling
    """
    board = [
['x','o','x','o','o','o','x','o'],
['o','o','x','o','o','x','o','o'],
['o','x','x','o','x','x','o','x'],
['o','x','x','o','o','x','o','x'],
['o','x','x','x','o','x','o','x'],
['o','o','x','x','o','x','o','o'],
['x','o','o','o','o','o','x','o'],
['s','o','x','x','x','o','o','e']
]
    xStart = 0
    yStart = 0
    button1 = button((255,255,0),0,0,constants.SCREEN_WIDTH/3,30,"BFS")
    button2 = button((255,255,0),constants.SCREEN_WIDTH/3,0,constants.SCREEN_WIDTH/3,30,"DFS")
    button3 = button((255,255,0),2*constants.SCREEN_WIDTH/3,0,constants.SCREEN_WIDTH/3,30,"RESET")
    def get_tile_color(self,tile_contents):
        """
        checks the content of the tile to determine the color to fill it with
        Args:
            - tile_contents: the content of the current grid section

        Returns:
            -a tuple of the rgb values of the color
        """
        tile_color = ()
        if(tile_contents == 'x'):
            tile_color = gray
        elif(tile_contents == 'o'):
            tile_color = white
        elif(tile_contents == 's'):
            tile_color = green
        elif(tile_contents == 'e'):
            tile_color = red
        elif(tile_contents == 'v'):
            tile_color = yellow
        elif(tile_contents == 'p'):
            tile_color = constants.DARKGREEN
        return tile_color
    def valid_BFS(self,moves,surface):
        """
        checks if the next space on the grid is a valid space or not. It will not be valid if its out of bounds or if theres a wall ('x')

        Args:
            -moves: the moves needed to get to the next space in the sequence. Sequence of D - down, U - up, L - left, R - right
            -surface: the pygame display that is being drawn on
        Return:
            - whether or not the next space is a valid space or not
        """
        i = 0
        j = 0
        for x, row in enumerate(self.board):
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

            if not(0 <= j < len(self.board[0]) and 0 <= i < len(self.board)):
                return False
            elif (self.board[i][j] == "x"):
                return False
            if(self.board[i][j] != 's' and self.board[i][j] != 'e'):
                self.board[i][j] = 'v'
            self.redraw(surface,self.board)
            pygame.display.update()
        return True
    def find_end_BFS(self,moves,surface):
        """
        Checks if the current space is the exit to the maze or not.

        Args:
            -moves: the moves needed to get to the next space in the sequence. Sequence of D - down, U - up, L - left, R - right
            -surface: the pygame display that is being drawn on.
        
        Return:
            - whether or not the space is the exit.
        """
        i = 0
        j = 0
        if(moves == 'DLDDDDRDDL'):
            print("hello")
        for x, row in enumerate(self.board):
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
        if self.board[i][j] == 'e':
            print("Found: " + moves)
            self.get_path_BFS(surface,moves)
            return True

        return False
    def get_path_BFS(self,surface, path = ''):
        """
        gets the full path from the start to the exit

        Args:
            - surface: the pygame display that is being drawn on
            - path: the series of moves that are needed to get to the exit. Series of D, L, U, or R for Down, Left, Up, or Right respectively.
        
        Return:
            -None
        """
        i = 0
        j = 0
        for x, row in enumerate(self.board):
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
    
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if (i, j) in pos and self.board[i][j] != 'e':
                    print("+ ", end="")
                    self.board[i][j] = 'p'
                else:
                    print(col + " ", end="")
                    self.board[i][j] = self.board[i][j]
            print()
        self.redraw(surface,self.board)
    def reset(self,surface):
        """
        Resets the maze back to its original state

        Args:
            -surface: the pygame display that is being drawn on.

        Return:
            -None
        """
        self.board = [
                    ['x','o','x','o','o','o','x','o'],
                    ['o','o','x','o','o','x','o','o'],
                    ['o','x','x','o','x','x','o','x'],
                    ['o','x','x','o','o','x','o','x'],
                    ['o','x','x','x','o','x','o','x'],
                    ['o','o','x','x','o','x','o','o'],
                    ['x','o','o','o','o','o','x','o'],
                    ['s','o','x','x','x','o','o','e']
                    ]
        
        print("hello")
    def BFS(self,surface):
        """
        Performs the breadth first search on the maze to find the exit. Uses helper functions such as find_end_BFS() and valid_BFS().

        Args:
            - surface: the pygame window that is being drawn on.
        """
        nums = queue.Queue()
        nums.put("")
        add = ""
        while (not self.find_end_BFS(add,surface)):
            add = nums.get()
            for j in ["L", "R", "U", "D"]:
                put = add + j
                if self.valid_BFS(put,surface):
                    nums.put(put) 
    def DFS(self, x, y,surface):
        """
        Performs depth first search on the maze to find the exit

        Args:
            -x: the current x coordinate (row)
            -y: the current y coordinate (column)
            -surface: the pygame display that is being drawn on

        Return:
            -1 if/when the exit is found, 0 when the path leads to a dead end
        """
        if(x<0 or x>= 8 or y<0 or y>= 8):
            return 0
        if(self.board[x][y] == 'e'):
            return 1
        if(self.board[x][y] == 'v' or self.board[x][y] == 'x'):
            return 0
        self.board[x][y] = 'v'
        
        for i in self.board:
            print(i)
        print()
        self.redraw(surface,self.board)
        pygame.time.delay(500)
        pygame.display.update()
        if(self.DFS(x+1,y,surface)):
            self.board[x][y] = 'p'
            return 1
    
        if(self.DFS(x, y+1,surface)):
            self.board[x][y] = 'p'
            return 1
        if(self.DFS(x-1, y,surface)):
            self.board[x][y] = 'p'
            return 1
        if(self.DFS(x, y-1,surface)):
            self.board[x][y] = 'p'
            return 1
        self.redraw(surface,self.board)
        return 0
    def draw_map(self,surface,map_tiles):
        """
            draws and fills in the rectangles of the grid with appropriate colors

            Args:
                -surface: the pygame window
                -map_tiles: the 2d array that has values that will determine the color of each rectangle

            Return:
                -None
        """
        for i,tile in enumerate(map_tiles):
            for j,tile_contents in enumerate(tile):
                myrect = pygame.Rect(j*constants.BLOCK_WIDTH + 30,i*constants.BLOCK_HEIGHT + 30,constants.BLOCK_WIDTH,constants.BLOCK_HEIGHT)
                pygame.draw.rect(surface, self.get_tile_color(tile_contents),myrect)
    def draw_grid(self,surface):
        """
        Draws the grid lines to make it look more like a grid

        Args:
            -surface: The pygame window being drawn on

        Return:
            -None
        """
        for i in range(constants.NUMBER_OF_BLOCKS_WIDE):
            new_height = round(i*constants.BLOCK_HEIGHT) + 30
            new_width = round(i*constants.BLOCK_WIDTH) + 30
            pygame.draw.line(surface,black,(0,new_height),(constants.SCREEN_WIDTH,new_height),2)
            pygame.draw.line(surface,black,(new_width,0),(new_width,constants.SCREEN_HEIGHT),2)
        
        self.button1.draw(surface)
        self.button2.draw(surface)
        self.button3.draw(surface)
    def game_loop(self,surface, world_map):
        """
        main loop that is constantly running while the program is running. Checks for events to handle

        Args:
            -surface: The pygame window being drawn on
            -world_map: the 2d array that has values to determine the color of each rectangle

        Return:
            -None
        """
        while True:
            pygame.time.delay(500)
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if(self.button1.isOver(pos)):
                        print("Breadth First Search clicked!")
                        self.BFS(surface)
                        print("Hello")
                    elif(self.button2.isOver(pos)):
                        print("Depth First Search clicked!")
                        self.DFS(self.xStart,self.yStart,surface)
                        for i in self.board:
                            print(i)
                    elif(self.button3.isOver(pos)):
                        self.reset(surface)
                        self.redraw(surface,self.board)
                        pygame.display.update()
                        print("Reset Clicked!")
                        for i in self.board:
                            print(i)
            self.draw_map(surface, self.board)
            self.draw_grid(surface)
            pygame.display.update()
    def redraw(self, surface, board):
        """
        method to redraw and update the board when the algorithms are in progress

        Args:
            - surface: the pygame window that is being drawn on.
            -board: the 2 dimensional array that represents the maze.

        Return:
            -None
        """
        for i,tile in enumerate(board):
            for j,tile_contents in enumerate(tile):
                myrect = pygame.Rect(j*constants.BLOCK_WIDTH + 30,i*constants.BLOCK_HEIGHT + 30,constants.BLOCK_WIDTH,constants.BLOCK_HEIGHT)
                pygame.draw.rect(surface, self.get_tile_color(tile_contents),myrect)
        for i in range(constants.NUMBER_OF_BLOCKS_WIDE):
            new_height = round(i*constants.BLOCK_HEIGHT) + 30
            new_width = round(i*constants.BLOCK_WIDTH) + 30
            pygame.draw.line(surface,black,(0,new_height),(constants.SCREEN_WIDTH,new_height),2)
            pygame.draw.line(surface,black,(new_width,0),(new_width,constants.SCREEN_HEIGHT),2)
        
        self.button1.draw(surface)
        self.button2.draw(surface)
        self.button3.draw(surface)
    def initialize_game(self):
        """
        initialize the whole game and window

        Args:
            -None

        Return:
            the pygame window being drawn on
        """
        pygame.init()
        surface = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        pygame.display.set_caption(constants.TITLE)
        surface.fill(constants.BLACK)
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if(self.board[i][j] == 's'):
                    self.xStart = i
                    self.yStart = j
        
        return surface
    def main(self):
        """
        method that will be called in the main program to start and run everything

        Args:
            -None
        
        Return:
            -None
        """
        the_map = self.board
        surface = self.initialize_game()
        self.game_loop(surface, the_map)
game = Game()
game.main()






    