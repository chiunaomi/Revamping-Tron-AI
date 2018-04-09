import pygame
from pygame.locals import*
import time




class Cell(object):
    """Square object with area and location
    Used as building block for game grid"""
    def __init__(self, coords, cell_length):
        self.xrange = range(coords[0],coords[0]+cell_length)
        self.yrange = range(coords[1],coords[1]+cell_length)
    
