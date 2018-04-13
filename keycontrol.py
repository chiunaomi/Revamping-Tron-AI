"""
Controller class that takes player input and translates that to directions taken by the player objects.
""""

import pygame
from pygame.locals import*
import time

class KeyControl(object):
    """Assigns key strokes as actions and implements them in game model"""
    def __init__(self, model):
        self.model = model

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN and self.model.end_start == False:
            return True
        if event.type != KEYDOWN:
            return #if no keys were pressed it quits
        if event.key == pygame.K_LEFT and self.model.game_over != True:
            if self.model.player1.dir != "r":
                self.model.player1.dir = "l"
        if event.key == pygame.K_RIGHT and self.model.game_over != True:
            if self.model.player1.dir != "l":
                self.model.player1.dir = "r"
        if event.key == pygame.K_DOWN and self.model.game_over != True:
            if self.model.player1.dir != "u":
                self.model.player1.dir = "d"
        if event.key == pygame.K_UP and self.model.game_over != True:
            if self.model.player1.dir != "d":
                self.model.player1.dir = "u"

        if event.key ==pygame.K_a and self.model.game_over != True:
            if self.model.player2.dir != "r":
                self.model.player2.dir = "l"
        if event.key == pygame.K_d and self.model.game_over != True:
            if self.model.player2.dir != "l":
                self.model.player2.dir = "r"
        if event.key == pygame.K_s and self.model.game_over != True:
            if self.model.player2.dir != "u":
                self.model.player2.dir = "d"
        if event.key == pygame.K_w and self.model.game_over != True:
            if self.model.player2.dir != "d":
                self.model.player2.dir = "u"

        if event.key == pygame.K_SPACE and self.model.game_over == True:
            return True
