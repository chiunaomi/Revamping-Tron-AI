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
        self.end_start = False
        self.end_mode_setup = False
        self.end_player_setup = False
        self.end_multi1 = False
        self.end_multi2 = False
        self.game_start = False

    def handle_mode_setup(self, event):
        "Recognizes where the mouse is clicked on the mode setup screen to initiate the correct mode"
        if event.type != MOUSEBUTTONDOWN:
            return
        if event.type == MOUSEBUTTONDOWN and not self.end_mode_setup:
            cursor = pygame.mouse.get_pos()
            if cursor[0] > 145 and cursor[0] < 475:
                if cursor[1] > 200 and cursor[1] < 270:
                    self.model.mode = "single"
                    return True
                if cursor[1] > 300 and cursor[1] < 370:
                    self.model.mode = "multi"
                    return True

    def handle_single(self, event):
        "Recognizes where the mouse is clicked on the single player setup screen to initiate the correct number of AI opponents"
        if event.type != MOUSEBUTTONDOWN:
            return
        if event.type == MOUSEBUTTONDOWN and not self.end_player_setup:
            cursor = pygame.mouse.get_pos()
            if cursor[1] > 230 and cursor[1] < 280:
                if cursor[0] > 85 and cursor[0] < 135:
                    self.model.num_CPU = 1
                    return True
                if cursor[0] > 295 and cursor[0] < 345:
                    self.model.num_CPU = 2
                    return True
                if cursor[0] > 505 and cursor[0] < 555:
                    self.model.num_CPU = 3
                    return True

    def handle_multi1(self, event):
        "Recognizes where the mouse is clicked on the first multiplayer setup screen to initiate the correct number of players"
        if event.type != MOUSEBUTTONDOWN:
            return
        if event.type == MOUSEBUTTONDOWN and not self.end_player_setup:
            cursor = pygame.mouse.get_pos()
            if cursor[1] > 230 and cursor[1] < 280:
                if cursor[0] > 85 and cursor[0] < 135:
                    self.model.num_players = 2
                    return True
                if cursor[0] > 295 and cursor[0] < 345:
                    self.model.num_players = 3
                    return True
                if cursor[0] > 505 and cursor[0] < 555:
                    self.model.num_players = 4
                    return True

    def handle_multi2(self, event):
        "Recognizes where the mouse is clicked on the second multiplayer setup screen to initate the correct number of AI opponents"
        if event.type != MOUSEBUTTONDOWN:
            return
        if event.type == MOUSEBUTTONDOWN and not self.end_player_setup:
            cursor = pygame.mouse.get_pos()
            if cursor[1] > 230 and cursor[1] < 280:
                if self.model.num_players == 2:
                    if cursor[0] > 85 and cursor[0] < 135:
                        self.model.num_CPU = 0
                        return True
                    if cursor[0] > 295 and cursor[0] < 345:
                        self.model.num_CPU = 1
                        return True
                    if cursor[0] > 505 and cursor[0] < 555:
                        self.model.num_CPU = 2
                        return True
                if self.model.num_players == 3:
                    if cursor[0] > 240 and cursor[0] < 290:
                        self.model.num_CPU = 0
                        return True
                    if cursor[0] > 400 and cursor[0] < 450:
                        self.model.num_CPU = 1
                        return True

    def handle_event(self, event):
        "Controls all the key controls for each player and returns the correct direction string to the corresponding player object"
        if event.type != KEYDOWN:
            return #if no keys were pressed it quits

        if self.game_start and not self.model.game_over:
            if event.key == pygame.K_a and self.model.player1.alive:
                if self.model.player1.dir != "r":
                    self.model.player1.dir = "l"
            if event.key == pygame.K_d and self.model.player1.alive:
                if self.model.player1.dir != "l":
                    self.model.player1.dir = "r"
            if event.key == pygame.K_s and self.model.player1.alive:
                if self.model.player1.dir != "u":
                    self.model.player1.dir = "d"
            if event.key == pygame.K_w and self.model.player1.alive:
                if self.model.player1.dir != "d":
                    self.model.player1.dir = "u"

            if event.key == pygame.K_LEFT and self.model.player2.alive:
                if self.model.player2.dir != "r":
                    self.model.player2.dir = "l"
            if event.key == pygame.K_RIGHT and self.model.player2.alive:
                if self.model.player2.dir != "l":
                    self.model.player2.dir = "r"
            if event.key == pygame.K_DOWN and self.model.player2.alive:
                if self.model.player2.dir != "u":
                    self.model.player2.dir = "d"
            if event.key == pygame.K_UP and self.model.player2.alive:
                if self.model.player2.dir != "d":
                    self.model.player2.dir = "u"

            if event.key == pygame.K_v and self.model.player3.alive:
                if self.model.player3.dir != "r":
                    self.model.player3.dir = "l"
            if event.key == pygame.K_n and self.model.player3.alive:
                if self.model.player3.dir != "l":
                    self.model.player3.dir = "r"
            if event.key == pygame.K_b and self.model.player3.alive:
                if self.model.player3.dir != "u":
                    self.model.player3.dir = "d"
            if event.key == pygame.K_g and self.model.player3.alive:
                if self.model.player3.dir != "d":
                    self.model.player3.dir = "u"

            if event.key == pygame.K_k and self.model.player4.alive:
                if self.model.player4.dir != "r":
                    self.model.player4.dir = "l"
            if event.key == pygame.K_SEMICOLON and self.model.player4.alive:
                if self.model.player4.dir != "l":
                    self.model.player4.dir = "r"
            if event.key == pygame.K_l and self.model.player4.alive:
                if self.model.player4.dir != "u":
                    self.model.player4.dir = "d"
            if event.key == pygame.K_o and self.model.player4.alive:
                if self.model.player4.dir != "d":
                    self.model.player4.dir = "u"

        if event.key == pygame.K_SPACE and not self.end_start:
            return True
        if event.key == pygame.K_SPACE and self.model.game_over:
            return True
