"""
Main loop used to run our MVC.
"""

import pygame
from pygame.locals import*
import time
import os

from keycontrol import KeyControl
from player import Player
from cell import Cell
from pygamewindowview import PyGameWindowView
from tronmodel import TronModel
from BasicBotMovementUpdate import BasicBot

if __name__ == '__main__':

    def main_loop():
        """A nested loop which initializes the various setup screens and game and runs
        the model until the model's end game protocol is called. Hitting the space bar
        after a game ends reinitializes the loop which allows for a new match"""
        window =  pygame.display.set_mode((640,480))
        pygame.init()
        running = True
        while running:
            model = TronModel(10,640,480)
            view = PyGameWindowView(model,640,480)
            controller = KeyControl(model)
            end_start = False
            end_mode_setup = False
            end_player_setup = False
            game_over = False

            while not end_start:
                view.start_screen() #initiates first landing screen
                for event in pygame.event.get():
                    if event.type == QUIT: #if the window is closed, break out of the two while loops and go to pygame.quit()
                        running = False
                        end_start = True
                        end_mode_setup = True
                        end_player_setup = True
                        game_over = True
                    if controller.handle_event(event):
                        controller.end_start = True
                        end_start = True

            while not end_mode_setup:
                view.mode_setup() #initiates screen where player mode is chosen
                for event in pygame.event.get():
                    if event.type == QUIT:
                        running = False
                        end_mode_setup = True
                        end_player_setup = True
                        game_over = True
                    if controller.handle_mode_setup(event):
                        controller.end_mode_setup = True
                        end_mode_setup = True

            while not end_player_setup:
                if model.mode == "single": #if player mode is single player
                    model.num_players = 1
                    view.single_player_setup() #display single player opponent setup screen
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            running = False
                            end_player_setup = True
                            game_over = True
                        if controller.handle_single(event):
                            model.init_players()
                            controller.end_player_setup = True
                            end_player_setup = True
                            view.display_controls()
                            time.sleep(5)
                            view._init_draw()
                if model.mode == "multi": #if player mode is multiplayer
                    end_multi1 = False
                    while not end_multi1:
                        view.multi_player_setup1() #display player selection screen
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                running = False
                                end_player_setup = True
                                end_multi1 = True
                                end_multi2 = True
                                game_over = True
                            if controller.handle_multi1(event):
                                controller.end_multi1 = True
                                end_multi1 = True
                                if model.num_players == 4: #if there are 4 players, no bots can be initiated so skip bot initiation
                                    end_multi2 = True
                                else:
                                    end_multi2 = False
                    while not end_multi2:
                        view.multi_player_setup2() #display AI opponent selection screen
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                running = False
                                end_player_setup = True
                                end_multi2 = True
                                game_over = True
                            if controller.handle_multi2(event):
                                controller.end_multi2 = True
                                end_multi2 = True
                    model.init_players()
                    end_player_setup = True
                    view.display_controls() #display keyboard controls for players
                    time.sleep(5)
                    view._init_draw()

            pygame.display.flip()
            controller.game_start = True
            while not game_over:
                for event in pygame.event.get():
                    if event.type == QUIT: #if the window is closed, break out of the two while loops and go to pygame.quit()
                        running = False
                        game_over = True
                    if controller.handle_event(event): #checks to see if the game has ended and the spacebar was pressed, if yes then the inner loop is broken and the game is reinitialized
                        game_over = True
                    controller.handle_event(event) #handles regular keypress events
                model.update()
                view.draw()
                time.sleep(.1)

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
        pygame.quit()

main_loop()
