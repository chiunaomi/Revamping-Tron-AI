"""
Player class that defines the behavior of the players.
"""
import pygame
from pygame.locals import*
import time

class Player(object):
    """Contains player's location, direction and speed, as well as their color"""
    def __init__(self, draw_screen, dimension, start_posx, start_posy, direction, color_name, color=(255,255,255)):
        self.draw_screen = draw_screen
        self.width = dimension
        self.height = dimension
        self.x = start_posx
        self.y = start_posy
        self.vx = 0
        self.vy = 0
        self.dir = direction
        self.color = color
        self.name = color_name
        self.last_seen = None
        self.current_cell = None
        self.alive = True

    def draw(self):
        """Function that blits a rectangle onto the screen representing the player's current position.
        Is called by the pygamewindowview class' draw method"""
        line_width = .5
        pygame.draw.rect(self.draw_screen,self.color,pygame.Rect(self.x,self.y,self.width,self.height))

    def update(self):
        """Checks if players have changed directions, and then
        adds the correct number of pixels to the player's position in the relevant direction"""
        if self.dir == "r":
            self.vx = 10
            self.vy = 0
        elif self.dir == "l":
            self.vx = -10
            self.vy = 0
        elif self.dir == "u":
            self.vx = 0
            self.vy = -10
        elif self.dir == "d":
            self.vx = 0
            self.vy = 10
        elif self.dir == "None":
            self.vx = 0
            self.vy = 0
        self.x += self.vx
        self.y += self.vy
