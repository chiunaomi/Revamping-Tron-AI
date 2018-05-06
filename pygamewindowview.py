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
        self.black = (0,0,0)
        self.blue = (0, 150, 150)
        self.green = (0, 255, 0)
        self.font = pygame.font.Font(os.path.join(os.path.dirname(os.path.realpath(__file__)),'TRON.TTF'), 25)

    def start_screen(self):
        label1= self.font.render("Welcome to Tron Revamped", 1, self.blue)
        label2 = self.font.render("Press Space to Start", 1, self.green)
        self.model.screen.fill(self.black)
        self.model.screen.blit(label1,(10,100))
        self.model.screen.blit(label2,(60,200))
        pygame.display.flip()

    def mode_setup(self):
        label = self.font.render("Game Mode", 1, self.blue)
        one = pygame.Rect((145,200),(350,70))
        labelone = self.font.render("Single Player", 1, self.black)
        two = pygame.Rect((145,300),(350,70))
        labeltwo = self.font.render("Multiplayer", 1, self.black)
        self.model.screen.fill(self.black)
        pygame.draw.rect(self.model.screen,self.green,one,0)
        pygame.draw.rect(self.model.screen,self.green,two,0)
        self.model.screen.blit(label,(200,100))
        self.model.screen.blit(labelone,(157,210))
        self.model.screen.blit(labeltwo,(180,310))
        pygame.display.flip()

    def single_player_setup(self):
        self.model.screen.fill(self.black)
        side_length = (50,50)
        opponents = self.font.render("Number of Opponents", 1, self.blue)
        labelone = self.font.render("1", 1, self.black)
        labeltwo = self.font.render("2", 1, self.black)
        labelthree = self.font.render("3", 1, self.black)
        one = pygame.Rect((85, 230),side_length)
        two = pygame.Rect((295, 230),side_length)
        three = pygame.Rect((505, 230),side_length)
        self.model.screen.blit(opponents,(70,100))
        pygame.draw.rect(self.model.screen,self.green,one,0)
        pygame.draw.rect(self.model.screen,self.green,two,0)
        pygame.draw.rect(self.model.screen,self.green,three,0)
        self.model.screen.blit(labelone,(103,230))
        self.model.screen.blit(labeltwo,(306,230))
        self.model.screen.blit(labelthree,(516,230))
        pygame.display.flip()

    def multi_player_setup1(self):
        self.model.screen.fill(self.black)
        side_length = (50,50)
        players = self.font.render("Number of Players", 1, self.blue)
        labelone = self.font.render("2", 1, self.black)
        labeltwo = self.font.render("3", 1, self.black)
        labelthree = self.font.render("4", 1, self.black)
        one = pygame.Rect((85, 230),side_length)
        two = pygame.Rect((295, 230),side_length)
        three = pygame.Rect((505, 230),side_length)
        self.model.screen.blit(players,(99,100))
        pygame.draw.rect(self.model.screen,self.green,one,0)
        pygame.draw.rect(self.model.screen,self.green,two,0)
        pygame.draw.rect(self.model.screen,self.green,three,0)
        self.model.screen.blit(labelone,(96,230))
        self.model.screen.blit(labeltwo,(306,230))
        self.model.screen.blit(labelthree,(518,230))
        pygame.display.flip()

    def multi_player_setup2(self):
        self.model.screen.fill(self.black)
        side_length = (50,50)
        opponents = self.font.render("Number of CPUs", 1, self.blue)
        label = []
        rect = []
        font = []
        label.append(self.font.render("0", 1, self.black))
        label.append(self.font.render("1", 1, self.black))
        label.append(self.font.render("2", 1, self.black))
        if self.model.num_players == 2:
            rect.append((85,230))
            rect.append((295,230))
            rect.append((505,230))
            font.append((100,230))
            font.append((313,230))
            font.append((516,230))
        if self.model.num_players == 3:
            rect.append((240,230))
            rect.append((400,230))
            font.append((255,230))
            font.append((418,230))
        for i in range(len(rect)):
            rectangle = pygame.Rect(rect[i],side_length)
            pygame.draw.rect(self.model.screen,self.green,rectangle,0)
            self.model.screen.blit(label[i],font[i])
        self.model.screen.blit(opponents,(139,100))
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
