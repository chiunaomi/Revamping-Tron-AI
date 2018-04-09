import pygame
from pygame.locals import*
import time




class Cellview(object):
    """Cell object defining the visualized form of a cell.
    Not used structurally to define player locations, but used to visualize the game"""
    def __init__(self, draw_screen, coordinates, side_length):
        self.draw_screen = draw_screen
        self.coordinates = coordinates
        self.side_length = side_length
        self.color = (0, 0, 0)

    def draw(self):
        line_width = 1
        rect = pygame.Rect(self.coordinates, self.side_length)
        pygame.draw.rect(self.draw_screen, self.color, rect, line_width)
