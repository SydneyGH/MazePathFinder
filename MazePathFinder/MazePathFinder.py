import curses
from curses import wrapper
import queue
import time

maze = [
    ["*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", " ", " ", " ", " ", " ", " ", " ", "O"],
    ["*", " ", "*", "*", " ", "*", "*", " ", "*"],
    ["*", " ", "*", " ", " ", " ", "*", " ", "*"],
    ["*", " ", "*", " ", "*", " ", "*", " ", "*"],
    ["*", " ", "*", " ", "*", " ", "*", " ", "*"],
    ["*", " ", "*", " ", "*", " ", "*", "*", "*"],
    ["X", " ", " ", " ", " ", " ", " ", " ", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*"]
]

def printMaze(maze, stdscr, path=[]):
    # Print the maze to the screen
    blueBlack = curses.color_pair(1)
    yellowBlack = curses.color_pair(2)

    for i, row in enumerate(maze):
        for k, value in enumerate(row):
            if (i,k) in path:
                stdscr.addstr(i, k*2, "X", yellowBlack)
            else:
                stdscr.addstr(i, k*2, value, blueBlack)


def start(maze, point):
    # Write code to find the starting point for the path finder
    for i, row in enumerate(maze):
        for k, value in enumerate(row):
            if value == point:
                return i, k
    return None

def neighbor(maze, row, column):
    # Find all of the other nodes
    nextS = []
    if(row > 0):
        nextS.append((row - 1, column))
    if(row +1 < len(maze)):
        nextS.append((row + 1, column))
    if(column > 0):
        nextS.append((row, column - 1))
    if(column +1 < len(maze)):
        nextS.append((row, column + 1))

    return nextS

def shortPath(maze, stdscr):
    point = "O"
    end = "X"
    startPoint = start(maze, point)

    que = queue.Queue()
    que.put((startPoint, [startPoint]))
    visitPoint = set()

    while not que.empty():
        currentPoint, path = que.get()
        row, column = currentPoint

        stdscr.clear()
        printMaze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()

        if maze[row][column] == end:
            return path
        
        nextS = neighbor(maze, row, column)
        for nextP in nextS:
            if nextP in visitPoint:
                continue
        
            ro, col = nextP
            if maze[ro][col] == '*':
                continue
        
            newP = path + [nextP]
            que.put((nextP, newP))
            visitPoint.add(nextP)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
 
    shortPath(maze, stdscr)
    # whiteBlack = curses.color_pair(1)
    # yellowBlack = curses.color_pair(2)

    stdscr.getch()


wrapper(main)