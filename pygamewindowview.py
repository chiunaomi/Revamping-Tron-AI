"""
Contains the view class for our MVC structure.
View displays the model's state in the PyGame window.
"""
import pygame
from pygame.locals import*
import os
import time
from cell import Cell

class PyGameWindowView(object):
    """View object containing the visual elements of the game.
    Takes a game model and renders its state onscreen"""
    def __init__(self,model,width,height):
        self.model = model
        size = (width,height)
        self.model.screen = pygame.display.set_mode(size)
        self.font = pygame.font.Font(os.path.join(os.path.dirname(os.path.realpath(__file__)),'TRON.TTF'), 25)

    def start_screen(self):
        black = (0,0,0)
        label1= self.font.render("Welcome to Tron Revamped", 1, (0, 150, 150))
        label2 = self.font.render("Press Space to Start", 1, (0, 255, 0))
        self.model.screen.fill(black)
        self.model.screen.blit(label1,(10,100))
        self.model.screen.blit(label2,(60,200))
        pygame.display.flip()

    def setup_screen(self):
        black = (0,0,0)
        label = self.font.render("Number of Players", 1, (0, 150, 150))
        side_length = (50,50)
        color = (0, 255, 0)
        one = pygame.Rect((55,230),side_length)
        labelone = self.font.render("1", 1, black)
        two = pygame.Rect((215,230),side_length)
        labeltwo = self.font.render("2", 1, black)
        three = pygame.Rect((375,230),side_length)
        labelthree = self.font.render("3", 1, black)
        four = pygame.Rect((535,230),side_length)
        labelfour = self.font.render("4", 1, black)
        self.model.screen.fill(black)
        pygame.draw.rect(self.model.screen,color,one,0)
        pygame.draw.rect(self.model.screen,color,two,0)
        pygame.draw.rect(self.model.screen,color,three,0)
        pygame.draw.rect(self.model.screen,color,four,0)
        self.model.screen.blit(label,(100,100))
        self.model.screen.blit(labelone,(70,230))
        self.model.screen.blit(labeltwo,(225,230))
        self.model.screen.blit(labelthree,(388,230))
        self.model.screen.blit(labelfour,(548,230))
        pygame.display.flip()

    def _init_draw(self):
        """Draws the grid on the screen and is only called at the beginning of a game."""
        self.model.screen.fill((105,105,105))
        self.model.cells = {}
        cell_size = self.model.cell_length
        for i in range(self.model.height):
            for j in range(self.model.width):
                cell_coord = (i*self.model.cell_length,j*self.model.cell_length)
                self.model.cells[(i,j)] = Cell(self.model.screen,cell_coord,cell_size)
        all_cells = self.model.cells.values()
        for cell in all_cells:
            cell.draw()

    def draw(self):
        """Draws the player paths and is updated and redrawn constantly"""
        if not self.model.game_over:
            self.model._draw_players()
        pygame.display.update()
