"""
Contains the view class for our MVC structure.
View displays the model's state in the PyGame window.
"""
import pygame
from pygame.locals import*
import time
from cell import Cell

class PyGameWindowView(object):
    """View object containing the visual elements of the game.
    Takes a game model and renders its state onscreen"""
    def __init__(self,model,width,height):
        self.model = model
        size = (width,height)
        self.model.screen = pygame.display.set_mode(size)

    def start_screen(self):
        black = (0,0,0)
        myfont = pygame.font.SysFont("Britannic Bold", 50)
        label1= myfont.render("Welcome to Tron Revamped", 1, (0, 150, 150))
        label2 = myfont.render("Click to Start", 1, (0, 255, 0))
        self.model.screen.fill(black)
        self.model.screen.blit(label1,(90,100))
        self.model.screen.blit(label2,(200,200))
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
