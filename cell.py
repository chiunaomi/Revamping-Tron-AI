"""
Cell object used to draw the background grid and define the paths of the players.
"""
import pygame
from pygame.locals import*
import time

class Cell(object):
    """Cell object defining the visualized form of a cell.
    Not used structurally to define player locations, but used to visualize the game"""
    def __init__(self, draw_screen, coordinates, side_length):
        self.xrange = range(coordinates[0],coordinates[0]+side_length)
        self.yrange = range(coordinates[1],coordinates[1]+side_length)
        self.draw_screen = draw_screen
        self.coordinates = coordinates
        self.side_length = (side_length,side_length)
        self.color = (0, 0, 0)

    def draw(self):
        """Used for the pygamewindowview class' _init_draw method to draw the initial playing grid"""
        line_width = 1
        rect = pygame.Rect(self.coordinates, self.side_length)
        pygame.draw.rect(self.draw_screen, self.color, rect, line_width)
