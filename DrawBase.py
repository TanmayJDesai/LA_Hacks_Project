import sys 
import numpy as np 
from collections import deque 
import pygame

CONST_BASE = 1
CONST_GRID_SIZE_X = 50
CONST_GRID_SIZE_X = 50

def GridCheck(Grid, Row, Column): 
  if (Grid[Row][Column] == 0): 
    return True
  return False

def check(GRID, Visited, ROW, COLUMN): 
  M, N = GRID.shape
  
  #NEED TO DO ::
    #Create background insert of image(Maps)
    #Add in drop down menu and various maps --> Google Maps API
    #Block anything inside the set barriers 
    
    check1 = (ROW >= 0)
    check2 = (ROW < M)
    check3 = (COLUMN >= 0)
    check4 = (COLUMN < N)
    
    if isinstance(Visited, dict): 
      return check1 and check2 and check3 and check4 and GridCheck(GRID, ROW, COLUMN) and not Visited.get((ROW, COLUMN), False)
    else: 
      check5 = (GRID[ROW][COLUMN] == 0)
      return check1 and check2 and check3 and check4 and check5 and not Visited[ROW][COLUMN]
