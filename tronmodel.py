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
from BasicBotMovementUpdate import BasicBot

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
        self.mode = None
        self.num_players = 0
        self.num_CPU = 0

    def init_players(self):
        "Initiates number of players and AI bots specified by user input"
        x_pos = [(self.width/2-100),(self.width/2+100)]
        s_dir = ["l","r"]
        if self.num_players + self.num_CPU == 2:
            y_pos = [(self.height/2),(self.height/2)]
        else:
            y_pos = [(self.height/2-50),(self.height/2-50),(self.height/2+50),(self.height/2+50)]
        if self.num_players == 0:
            return
        if self.num_players == 1:
            self.player1 = Player(self.screen,10,x_pos[0],y_pos[0],s_dir[0],self.color_strings[0],self.player_colors[0])
            self.players = [self.player1]
        if self.num_players == 2:
            self.player1 = Player(self.screen,10,x_pos[0],y_pos[0],s_dir[0],self.color_strings[0],self.player_colors[0])
            self.player2 = Player(self.screen,10,x_pos[1],y_pos[1],s_dir[1],self.color_strings[1],self.player_colors[1])
            self.players = [self.player1,self.player2]
        if self.num_players == 3:
            self.player1 = Player(self.screen,10,x_pos[0],y_pos[0],s_dir[0],self.color_strings[0],self.player_colors[0])
            self.player2 = Player(self.screen,10,x_pos[1],y_pos[1],s_dir[1],self.color_strings[1],self.player_colors[1])
            self.player3 = Player(self.screen,10,x_pos[0],y_pos[2],s_dir[0],self.color_strings[2],self.player_colors[2])
            self.players = [self.player1,self.player2,self.player3]
        if self.num_players == 4:
            self.player1 = Player(self.screen,10,x_pos[0],y_pos[0],s_dir[0],self.color_strings[0],self.player_colors[0])
            self.player2 = Player(self.screen,10,x_pos[1],y_pos[1],s_dir[1],self.color_strings[1],self.player_colors[1])
            self.player3 = Player(self.screen,10,x_pos[0],y_pos[2],s_dir[0],self.color_strings[2],self.player_colors[2])
            self.player4 = Player(self.screen,10,x_pos[1],y_pos[3],s_dir[1],self.color_strings[3],self.player_colors[3])
            self.players = [self.player1,self.player2,self.player3,self.player4]
        if self.num_CPU == 0:
            self.bots = []
        if self.num_CPU == 1:
            self.bot1 = BasicBot(self,self.screen,10,x_pos[self.num_players%2],y_pos[self.num_players],s_dir[self.num_players%2],self.color_strings[self.num_players],self.player_colors[self.num_players])
            self.bots = [self.bot1]
        if self.num_CPU == 2:
            self.bot1 = BasicBot(self,self.screen,10,x_pos[self.num_players%2],y_pos[self.num_players],s_dir[self.num_players%2],self.color_strings[self.num_players],self.player_colors[self.num_players])
            self.bot2 = BasicBot(self,self.screen,10,x_pos[(self.num_players+1)%2],y_pos[self.num_players+1],s_dir[(self.num_players+1)%2],self.color_strings[self.num_players+1],self.player_colors[self.num_players+1])
            self.bots = [self.bot1,self.bot2]
        if self.num_CPU == 3:
            self.bot1 = BasicBot(self,self.screen,10,x_pos[self.num_players%2],y_pos[self.num_players],s_dir[self.num_players%2],self.color_strings[self.num_players],self.player_colors[self.num_players])
            self.bot2 = BasicBot(self,self.screen,10,x_pos[(self.num_players+1)%2],y_pos[self.num_players+1],s_dir[(self.num_players+1)%2],self.color_strings[self.num_players+1],self.player_colors[self.num_players+1])
            self.bot3 = BasicBot(self,self.screen,10,x_pos[(self.num_players+2)%2],y_pos[self.num_players+2],s_dir[(self.num_players+2)%2],self.color_strings[self.num_players+2],self.player_colors[self.num_players+2])
            self.bots = [self.bot1,self.bot2,self.bot3]

    def _draw_players(self):
        """Calls the player and bot objects' draw functions"""
        for player in self.players:
            player.draw()
        for bot in self.bots:
            bot.draw()

    def in_cell(self):
        """Loops through cell_lst to find the cell whose xrange contains player.x or bot.x
        and whose yrange contains player.y or bot.y, and sets the player/bot location to be within that cell."""
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
            bot.random_choice_move() #bot performs depth search and chooses the best direction
            bot.last_seen = bot.current_cell

        self.in_cell() #updates the cell locations of each player/bot
        for player in self.players:
            if player.current_cell != player.last_seen:
                self.player_paths.add(player.last_seen)
        #If the player has left a cell and moved into another, the vacated cell is
        #added to the list of cells that have been hit
            if player.current_cell in self.player_paths:
                self.players.remove(player)
                player.alive = False
        #If the player's location is in the list of cells
        #that already have been traversed, the player is removed from play
        for bot in self.bots:
            if bot.current_cell != bot.last_seen:
                self.player_paths.add(bot.last_seen)
            if bot.current_cell in self.player_paths:
                self.bots.remove(bot)
                print(self.bots)
                bot.alive = False
        if len(self.players) + len(self.bots) == 1:#checks to see if there is only 1 player/bot left in the game
            if len(self.players) == 1:
                self.end_game(self.players[0].name,self.players[0].color)
            if len(self.bots) == 1:
                self.end_game(self.bots[0].name,self.bots[0].color)

    def end_game(self,player,color):
        """Contains end game protocol and end game display."""
        black = (0, 0, 0)
        font = pygame.font.Font(os.path.join(os.path.dirname(os.path.realpath(__file__)),'Tr2n.ttf'), 70)
        font2 = pygame.font.Font(os.path.join(os.path.dirname(os.path.realpath(__file__)),'Tr2n.ttf'), 35)
        label1= font.render(player + " WINS!", 1, color)
        label2 = font2.render("Press Space to Restart", 1, (255,255,255))
        self.screen.fill(black)
        self.screen.blit(label1,((self.width-font.size(player + " WINS!")[0])/2,100))
        self.screen.blit(label2,((self.width-font2.size("Press Space to Restart")[0])/2,200))
        pygame.display.flip()
        self.game_over = True
        for player in self.players:
            player.dir = "None"
