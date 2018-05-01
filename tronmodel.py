"""
Contains the model class for our MVC structure.
Model updates the state of the game.
"""

import pygame
from pygame.locals import*
import time
import os

from player import Player
from cell import Cell

class TronModel(object):
    """Model object containing the players, the game state, all cells, and the cells that have been hit."""
    def __init__(self,cell_length,width,height):
        pygame.init()
        size = (width,height)
        self.screen = pygame.display.set_mode(size)
        self.width = width
        self.height = height
        self.cell_length = cell_length
        self.cell_lst = []
        self.player_paths = []
        self.player1 = Player(self.screen,10,(self.width/2+100),(self.height/2),"r",(255,140,0))
        self.player2 = Player(self.screen,10,(self.width/2-100),(self.height/2),"l",(0,250,0))
        for i in range(self.height//cell_length):
            for j in range(self.width//cell_length):
                self.cell_lst.append(Cell(self.screen,(i*self.cell_length,j*self.cell_length),cell_length))
        self.game_over = False
        self.end_start = False
        self.end_setup = False

    def _draw_players(self):
        """Calls the player objects' draw functions"""
        self.player1.draw()
        self.player2.draw()

    def in_cell(self):
        """Loops through cell_lst to find the cell whose xrange contains player.x
        and whose yrange contains player.y, and sets the player location to be within that cell."""
        for cell in self.cell_lst:
            if self.player1.x in cell.xrange and self.player1.y in cell.yrange:
                self.player1.current_cell = cell
                break
        for cell in self.cell_lst:
            if self.player2.x in cell.xrange and self.player2.y in cell.yrange:
                self.player2.current_cell = cell
                break

    def update(self):
        """Checks for new inputs and updates the game model."""
        self.player1.update()
        self.player2.update()
        if self.player1.crash():
            self.end_game("GREEN ",(0,250,0))
        if self.player2.crash():
            self.end_game("ORANGE ",(255,140,0))

        last_seen_p1 = self.player1.current_cell
        last_seen_p2 = self.player2.current_cell
        # Saving the player locations before updating in order to test to see if the players
        # have entered a new cell.
        self.in_cell()
        if self.player1.current_cell != last_seen_p1:
            self.player_paths.append(last_seen_p1)
        if self.player2.current_cell != last_seen_p2:
            self.player_paths.append(last_seen_p2)
        #If the player has left a cell and moved into another, the vacated cell is
        #added to the list of cells that have been hit

        if self.player1.current_cell in self.player_paths:
            self.end_game("GREEN ",(0,250,0))
        if self.player2.current_cell in self.player_paths:
            self.end_game("ORANGE ",(255,140,0))

    def end_game(self,player,color):
        """Contains end game protocol and end game display."""
        black = (0, 0, 0)
        font = pygame.font.Font(os.path.join(os.path.dirname(os.path.realpath(__file__)),'TRON.TTF'), 25)
        label1= font.render(player + "WINS!", 1, color)
        label2 = font.render("Press Space to Restart", 1, (255,255,255))
        self.screen.fill(black)
        self.screen.blit(label1,(185,100))
        self.screen.blit(label2,(43,200))
        pygame.display.flip()
        self.game_over = True
        self.player1.dir = "None"
        self.player2.dir = "None"
