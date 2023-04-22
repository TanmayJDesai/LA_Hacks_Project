import sys
import numpy as np
from collections import deque
import pygame

CONST_INT = 1
GRID_SIZE_X = 50
GRID_SIZE_Y = 50

def GridCheck(Grid, Row, Column):
    if (Grid[Row][Column] == 0):
        return True
    return False
def check(GRID, Visited, ROW, COLUMN):
    M, N = GRID.shape


    #Create background insert of image


    #Find photo of UCLA Campus and outline all buildings
    #Make those outlines permanant
    #Block anything inside those barriers.


    check1 = (ROW >= 0)
    check2 = (ROW < M)
    check3 = (COLUMN >= 0)
    check4 = (COLUMN < N)
    if isinstance(Visited, dict):
        return check1 and check2 and check3 and check4 and GridCheck(GRID, ROW, COLUMN) and not Visited.get((ROW, COLUMN), False)
    else:
        check5 = (GRID[ROW][COLUMN] == 0)
        return check1 and check2 and check3 and check4 and check5 and not Visited[ROW][COLUMN]

def FIND_SHORTEST_PATH(point, PointList, Wall):
    start, end = PointList
    STARTX, STARTY = start
    ENDX, ENDY = end
    GRIDSHAPE = np.zeros([GRID_SIZE_X, GRID_SIZE_Y])
    for i in Wall:
        GRIDSHAPE[i] = CONST_INT
    M, N = GRIDSHAPE.shape

    # explore 4 neighbors
    ROW = [-1, 0, 0, 1]
    COLUMN = [0, -1, 1, 0]
    LUDR = ['L', 'U', 'D', 'R']
    QUIT = deque()

    visited = {}
    visited[(STARTX, STARTY)] = True
    COMBINE = ""
    QUIT.append((STARTX, STARTY, 0, COMBINE))
    DISTANCE = sys.maxsize

    while QUIT:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        (START_X, START_Y, DIST, COMBINE) = QUIT.popleft()
        FIRST_CONDITION = START_X == ENDX
        SECOND_CONDITION = START_Y == ENDY
        FINAL_CONDITION = FIRST_CONDITION and SECOND_CONDITION
        if FINAL_CONDITION:
            DISTANCE = DIST
            break
        for a in range(4):
            if check(GRIDSHAPE, visited, START_X + ROW[a], START_Y + COLUMN[a]):
                NEW = (START_X + ROW[a], START_Y + COLUMN[a])
                visited[NEW] = True
                #NOTE: Uncomment this chunk of code if you would like to mark the path of the tester.
                #point.write('.', NEW[0], NEW[CONST_INT], fgcolor='blue')
                QUIT.append((NEW[0], NEW[CONST_INT], DIST + CONST_INT, COMBINE + LUDR[a]))

    point.write('✓', ENDX, ENDY)

    if DISTANCE != sys.maxsize:
        # find path
        start_x, start_y = PointList[0]
        for i in range(len(COMBINE)):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            index = LUDR.index(COMBINE[i])
            start_x, start_y = start_x + ROW[index], start_y + COLUMN[index]
            point.write('+', start_x, start_y, fgcolor='yellow')
        point.write('✓', ENDX, ENDY)
        point.write(f"We found a path using BFS! It is {DISTANCE} units", CONST_INT, CONST_INT)
    else:
        point.write("No path exists because of the barriers! Please try again", CONST_INT, CONST_INT)
