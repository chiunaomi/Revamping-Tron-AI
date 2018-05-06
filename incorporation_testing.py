import pygame
from pygame.locals import*
from cell import Cell

node = (range(20, 30),range(60,70))
def next_to(node):
    left = (range(node[0][0]-10,node[0][9]-9),node[1])
    right = (range(node[0][0]+10,node[0][9]+11),node[1])
    top = (node[0],range(node[1][0]+10,node[1][9]+11))
    bottom = (node[0],range(node[1][0]-10,node[1][9]-9))
    print(left)
    print(right)
    print(top)
    print(bottom)

next_to(node)
