import pygcurse
import pygame
from pygame.locals import *
import sys
import numpy as np
from bfs import FIND_SHORTEST_PATH
CONST_INT = 2

def create_grid(Row, Column):
    #Create a pygame app of grids
    GridPattern = np.empty((Row, Column), dtype=str)
    #Make all the grids empty
    GridPattern[:] = " "
    #Create certain sized (as I specify)grids using the - and | characters
    for i in range(0, Row, 50):
        for j in range(Column):
            GridPattern[i][j] = '-'
    for i in range(0, Column, 50):
        for j in range(Column):
            GridPattern[j][i] = '|'
    #Return this pattern to be drawn.
    return GridPattern

def Draw_The_Grid(Game, Final_Grid):
    #Just use a nested for loop to create the grid background in the pygame.
    for i in range(Final_Grid.shape[0]):
        for j in range(Final_Grid.shape[1]):
            Game.write(Final_Grid[i][j], x=i, y=j)

def Final_Grid():
    grid_rows, grid_cols = 49, 49  # Updated to smaller grid size
    grid = np.empty((grid_rows, grid_cols), dtype=str)
    grid[:] = " "

    # Draw the horizontal lines
    for i in range(0, grid_rows, 5):  # Updated to smaller grid size
        for j in range(grid_cols):
            grid[i][j] = '-'

    #Draw the vertical lines
    for i in range(0, grid_cols, 5):  # Updated to smaller grid size
        for j in range(grid_rows):
            grid[j][i] = '|'

    # Create the Pygcurse window and set the screen colors
    point = pygcurse.PygcurseWindow(grid_rows, grid_cols, fgcolor='Orange')
    point.setscreencolors(None, 'black', clear=True)

    # Draw the grid on the screen
    for i in range(grid_rows):
        for j in range(grid_cols):
            point.write(grid[i][j], x=i, y=j)

    drag = False  # Initialize drag to False
    PointList = []
    while len(PointList) < CONST_INT:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                CurLocation = point.getcoordinatesatpixel(event.pos)
                point.write('✓', *CurLocation)
                PointList.append(CurLocation)

            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

    walls = set()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                drag = True
            elif event.type == pygame.MOUSEBUTTONUP:
                drag = False
            elif event.type == pygame.MOUSEMOTION:
                if drag:
                    coordinate = point.getcoordinatesatpixel(event.pos)
                    point.write('>', *coordinate)
                    walls.add(coordinate)
            elif event.type == pygame.KEYDOWN:
                    FIND_SHORTEST_PATH(point, PointList, walls)

if __name__ == "__main__":
    Final_Grid()
