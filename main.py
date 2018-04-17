"""
Main loop used to run our MVC.
"""

import pygame
from pygame.locals import*
import time

from keycontrol import KeyControl
from player import Player
from cell import Cell
from pygamewindowview import PyGameWindowView
from tronmodel import TronModel

if __name__ == '__main__':

    def main_loop():
        """A nested loop which initializes the game and runs the model until the end game protocol is called.
        Hitting the space bar after a game ends reinitializes the loop which allows for a new match"""
        window =  pygame.display.set_mode((640,480))
        pygame.init()
        running = True
        while running:
            model = TronModel(10,640,480)
            view = PyGameWindowView(model,640,480)
            controller = KeyControl(model)
            end_start = False
            game_over = False

            while not end_start:
                view.start_screen()
                for event in pygame.event.get():
                    if event.type == QUIT: #if the window is closed, break out of the two while loops and go to pygame.quit()
                        running = False
                        end_start = True
                        game_over = True
                    if controller.handle_event(event):
                        model.end_start = True
                        end_start = True
            view._init_draw()

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
