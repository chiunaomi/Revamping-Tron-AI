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
from BasicBotMovementUp import*

class TronModel(object):
    """Model object containing the players, the game state, all cells, and the cells that have been hit."""
    def __init__(self,cell_length,width,height):
        pygame.init()
        size = (width,height)
        self.screen = pygame.display.set_mode(size)
        self.width = width
        self.height = height
        self.cell_length = cell_length
        self.cell_lst = set()
        self.player_paths = set()
        for i in range(self.width//cell_length):
            for j in range(self.height//cell_length):
                cell = Cell(self.screen,(i*self.cell_length,j*self.cell_length),cell_length)
                self.cell_lst.add((cell.xrange,cell.yrange))
        for i in range(self.height//cell_length):
            cell = Cell(self.screen,(-10,i*self.cell_length),cell_length)
            self.cell_lst.add((cell.xrange,cell.yrange))
            self.player_paths.add((cell.xrange,cell.yrange))
            cell = Cell(self.screen,(self.width,i*self.cell_length),cell_length)
            self.cell_lst.add((cell.xrange,cell.yrange))
            self.player_paths.add((cell.xrange,cell.yrange))
        for j in range(self.width//cell_length):
            cell = Cell(self.screen,(j*self.cell_length,-10),cell_length)
            self.cell_lst.add((cell.xrange,cell.yrange))
            self.player_paths.add((cell.xrange,cell.yrange))
            cell = Cell(self.screen,(j*self.cell_length,self.height),cell_length)
            self.cell_lst.add((cell.xrange,cell.yrange))
            self.player_paths.add((cell.xrange,cell.yrange))
        self.player_colors = [(255,140,0),(0,250,0),(0,150,150),(255,0,0)]
        self.color_strings = ["Orange","Green","Blue","Red"]
        self.game_over = False
        self.end_start = False
        self.end_setup = False

    def init_players(self):
        "Initiates number of players specified by user input"
        if self.num_players == 1:
            self.player1 = Player(self.screen,10,(self.width/2-100),(self.height/2),"l",self.color_strings[0],self.player_colors[0])
            self.bot1 = BasicBot(self.screen,10,(self.width/2+100),(self.height/2),"r",self.color_strings[1],self.player_colors[1])
            self.players = [self.player1]
            self.bots = [self.bot1]
            print(self.players)
        if self.num_players == 2:
            self.player1 = Player(self.screen,10,(self.width/2-100),(self.height/2),"l",self.color_strings[0],self.player_colors[0])
            self.player2 = Player(self.screen,10,(self.width/2+100),(self.height/2),"r",self.color_strings[1],self.player_colors[1])
            self.players = [self.player1,self.player2]
            print(self.players)
        if self.num_players == 3:
            self.player1 = Player(self.screen,10,(self.width/2-100),(self.height/2-50),"l",self.color_strings[0],self.player_colors[0])
            self.player2 = Player(self.screen,10,(self.width/2+100),(self.height/2-50),"r",self.color_strings[1],self.player_colors[1])
            self.player3 = Player(self.screen,10,(self.width/2-100),(self.height/2+50),"l",self.color_strings[2],self.player_colors[2])
            self.players = [self.player1,self.player2,self.player3]
            print(self.players)
        if self.num_players == 4:
            self.player1 = Player(self.screen,10,(self.width/2-100),(self.height/2-50),"l",self.color_strings[0],self.player_colors[0])
            self.player2 = Player(self.screen,10,(self.width/2+100),(self.height/2-50),"r",self.color_strings[1],self.player_colors[1])
            self.player3 = Player(self.screen,10,(self.width/2-100),(self.height/2+50),"l",self.color_strings[2],self.player_colors[2])
            self.player4 = Player(self.screen,10,(self.width/2+100),(self.height/2+50),"r",self.color_strings[3],self.player_colors[3])
            self.players = [self.player1,self.player2,self.player3,self.player4]
            print(self.players)

    def _draw_players(self):
        """Calls the player objects' draw functions"""
        for player in self.players:
            player.draw()
        for bot in self.bots:
            bot.draw()

    def in_cell(self):
        """Loops through cell_lst to find the cell whose xrange contains player.x
        and whose yrange contains player.y, and sets the player location to be within that cell."""
        for player in self.players:
            for cell in self.cell_lst:
                if player.x in cell[0] and player.y in cell[1]:
                    player.current_cell = cell
                    break
        for bot in self.bots:
            for cell in self.cell_lst:
                if bot.x in cell[0] and bot.y in cell[1]:
                    bot.current_cell = cell
                    break

    def update(self):
        """Checks for new inputs and updates the game model."""
        for player in self.players:
            player.update()
            player.last_seen = player.current_cell
        for bot in self.bots:
            bot.random_choice_move(self.player_paths)
            bot.last_seen = bot.current_cell

        self.in_cell()
        for player in self.players:
            if player.current_cell != player.last_seen:
                self.player_paths.add(player.last_seen)
        #If the player has left a cell and moved into another, the vacated cell is
        #added to the list of cells that have been hit
            if player.current_cell in self.player_paths:
                self.players.remove(player)
                player.alive = False
        for bot in self.bots:
            if bot.current_cell != bot.last_seen:
                self.player_paths.add(bot.last_seen)
        #If the player has left a cell and moved into another, the vacated cell is
        #added to the list of cells that have been hit
            if bot.current_cell in self.player_paths:
                self.bots.remove(bot)
                print(self.bots)
                bot.alive = False
        if len(self.players) + len(self.bots) == 1:
            if len(self.players) == 1:
                self.end_game(self.players[0].name,self.players[0].color)
            if len(self.bots) == 1:
                self.end_game(self.bots[0].name,self.bots[0].color)

    def end_game(self,player,color):
        """Contains end game protocol and end game display."""
        black = (0, 0, 0)
        font = pygame.font.Font(os.path.join(os.path.dirname(os.path.realpath(__file__)),'TRON.TTF'), 25)
        label1= font.render(player + " WINS!", 1, color)
        label2 = font.render("Press Space to Restart", 1, (255,255,255))
        self.screen.fill(black)
        self.screen.blit(label1,(185,100))
        self.screen.blit(label2,(43,200))
        pygame.display.flip()
        self.game_over = True
        for player in self.players:
            player.dir = "None"
