"""
Controller class that takes player input and translates that to directions taken by the player objects.
"""

import pygame
from pygame.locals import*
import time

class KeyControl(object):
    """Assigns key strokes as actions and implements them in game model"""
    def __init__(self, model):
        self.model = model

    def handle_setup(self, event):
        if event.type != MOUSEBUTTONDOWN:
            return
        if event.type == MOUSEBUTTONDOWN and self.model.end_setup == False:
            cursor = pygame.mouse.get_pos()
            if cursor[1] > 250 and cursor[1] < 300:
                if cursor[0] > 55 and cursor[0] < 105:
                    self.model.num_players = 1
                    return True
                if cursor[0] > 215 and cursor[0] < 265:
                    self.model.num_players = 2
                    return True
                if cursor[0] > 375 and cursor[0] < 435:
                    self.model.num_players = 3
                    return True
                if cursor[0] > 535 and cursor[0] < 585:
                    self.model.num_players = 4
                    return True

    def handle_event(self, event):
        if event.type != KEYDOWN:
            return #if no keys were pressed it quits

        if event.key == pygame.K_a and self.model.player1.alive == True and self.model.game_over != True:
            if self.model.player1.dir != "r":
                self.model.player1.dir = "l"
        if event.key == pygame.K_d and self.model.player1.alive == True and self.model.game_over != True:
            if self.model.player1.dir != "l":
                self.model.player1.dir = "r"
        if event.key == pygame.K_s and self.model.player1.alive == True and self.model.game_over != True:
            if self.model.player1.dir != "u":
                self.model.player1.dir = "d"
        if event.key == pygame.K_w and self.model.player1.alive == True and self.model.game_over != True:
            if self.model.player1.dir != "d":
                self.model.player1.dir = "u"

        if event.key == pygame.K_LEFT and self.model.player2.alive == True and self.model.game_over != True:
            if self.model.player2.dir != "r":
                self.model.player2.dir = "l"
        if event.key == pygame.K_RIGHT and self.model.player2.alive == True and self.model.game_over != True:
            if self.model.player2.dir != "l":
                self.model.player2.dir = "r"
        if event.key == pygame.K_DOWN and self.model.player2.alive == True and self.model.game_over != True:
            if self.model.player2.dir != "u":
                self.model.player2.dir = "d"
        if event.key == pygame.K_UP and self.model.player2.alive == True and self.model.game_over != True:
            if self.model.player2.dir != "d":
                self.model.player2.dir = "u"

        if event.key == pygame.K_v and self.model.player3.alive == True and self.model.game_over != True:
            if self.model.player3.dir != "r":
                self.model.player3.dir = "l"
        if event.key == pygame.K_n and self.model.player3.alive == True and self.model.game_over != True:
            if self.model.player3.dir != "l":
                self.model.player3.dir = "r"
        if event.key == pygame.K_b and self.model.player3.alive == True and self.model.game_over != True:
            if self.model.player3.dir != "u":
                self.model.player3.dir = "d"
        if event.key == pygame.K_g and self.model.player3.alive == True and self.model.game_over != True:
            if self.model.player3.dir != "d":
                self.model.player3.dir = "u"

        if event.key == pygame.K_k and self.model.player4.alive == True and self.model.game_over != True:
            if self.model.player4.dir != "r":
                self.model.player4.dir = "l"
        if event.key == pygame.K_l and self.model.player4.alive == True and self.model.game_over != True:
            if self.model.player4.dir != "l":
                self.model.player4.dir = "r"
        if event.key == pygame.K_k and self.model.player4.alive == True and self.model.game_over != True:
            if self.model.player4.dir != "u":
                self.model.player4.dir = "d"
        if event.key == pygame.K_i and self.model.player4.alive == True and self.model.game_over != True:
            if self.model.player4.dir != "d":
                self.model.player4.dir = "u"

        if event.key == pygame.K_SPACE and self.model.end_start == False:
            return True
        if event.key == pygame.K_SPACE and self.model.game_over == True:
            return True
