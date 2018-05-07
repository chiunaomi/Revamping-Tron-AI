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
        self.solid_font = pygame.font.Font(os.path.join(os.path.dirname(os.path.realpath(__file__)),'TRON.TTF'), 25)
        self.font = pygame.font.Font(os.path.join(os.path.dirname(os.path.realpath(__file__)),'Tr2n.ttf'), 35)
        self.xlarge_font = pygame.font.Font(os.path.join(os.path.dirname(os.path.realpath(__file__)),'Tr2n.ttf'), 70)
        self.large_font = pygame.font.Font(os.path.join(os.path.dirname(os.path.realpath(__file__)),'Tr2n.ttf'), 45)
        self.small_font = pygame.font.Font(os.path.join(os.path.dirname(os.path.realpath(__file__)),'Tr2n.ttf'), 25)

    def start_screen(self):
        label1= self.font.render("Welcome to Tron Revamped", 1, self.blue)
        label2 = self.font.render("Press Space to Start", 1, self.green)
        self.model.screen.fill(self.black)
        self.model.screen.blit(label1,((self.model.width-self.font.size("Welcome to Tron Revamped")[0])/2,100))
        self.model.screen.blit(label2,((self.model.width-self.font.size("Press Space to Start")[0])/2,200))
        pygame.display.flip()

    def mode_setup(self):
        label = self.xlarge_font.render("Game Mode", 1, self.blue)
        one = pygame.Rect(((self.model.width-380)/2,200),(380,70))
        labelone = self.large_font.render("Single Player", 1, self.black)
        two = pygame.Rect(((self.model.width-380)/2,300),(380,70))
        labeltwo = self.large_font.render("Multiplayer", 1, self.black)
        self.model.screen.fill(self.black)
        pygame.draw.rect(self.model.screen,self.green,one,0)
        pygame.draw.rect(self.model.screen,self.green,two,0)
        self.model.screen.blit(label,((self.model.width-self.xlarge_font.size("Game Mode")[0])/2,100))
        self.model.screen.blit(labelone,((self.model.width-self.large_font.size("Single Player")[0])/2,int(70-self.large_font.size("Single Player")[1])/2+205))
        self.model.screen.blit(labeltwo,((self.model.width-self.large_font.size("Multiplayer")[0])/2,315))
        pygame.display.flip()

    def single_player_setup(self):
        self.model.screen.fill(self.black)
        side_length = (50,50)
        opponents = self.font.render("Number of Opponents", 1, self.blue)
        labelone = self.solid_font.render("1", 1, self.black)
        labeltwo = self.solid_font.render("2", 1, self.black)
        labelthree = self.solid_font.render("3", 1, self.black)
        one = pygame.Rect((85, 230),side_length)
        two = pygame.Rect((295, 230),side_length)
        three = pygame.Rect((505, 230),side_length)
        self.model.screen.blit(opponents,((self.model.width-self.font.size("Number of Opponents")[0])/2,100))
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
        labelone = self.solid_font.render("2", 1, self.black)
        labeltwo = self.solid_font.render("3", 1, self.black)
        labelthree = self.solid_font.render("4", 1, self.black)
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
        label.append(self.solid_font.render("0", 1, self.black))
        label.append(self.solid_font.render("1", 1, self.black))
        label.append(self.solid_font.render("2", 1, self.black))
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

    def display_controls(self):
        self.model.screen.fill(self.black)
        controls = self.font.render("Player Controls",1,(255,255,255))
        loading = self.font.render("Loading...", 1, (255,255,255))
        players = ["Player 1","Player 2","Player 3","Player 4"]
        player_loc = []
        player_loc.append((int((self.model.width/2-self.small_font.size(players[0])[0])/2),70))
        player_loc.append((int((self.model.width/2-self.small_font.size(players[1])[0])/2+self.model.width/2),70))
        player_loc.append((int((self.model.width/2-self.small_font.size(players[2])[0])/2),250))
        player_loc.append((int((self.model.width/2-self.small_font.size(players[3])[0])/2+self.model.width/2),250))
        side_length = (40,40)
        down_rect_loc = []
        down_rect_loc.append((int((self.model.width/2-side_length[0])/2),180))
        down_rect_loc.append((int((self.model.width/2-side_length[0])/2+self.model.width/2),180))
        down_rect_loc.append((int((self.model.width/2-side_length[0])/2),350))
        down_rect_loc.append((int((self.model.width/2-side_length[0])/2+self.model.width/2),350))
        control_keys = [("s","a","d","w"),("\u2BC6","\u2BC7","\u2BC7","\u2BC5"),("b","v","n","g"),("l","k",":","o")]
        if self.model.num_players != None:
            for i in range(self.model.num_players):
                player = self.small_font.render(players[i],1,self.model.player_colors[i])
                loc = player_loc[i]
                self.model.screen.blit(player,loc)
                down_button = pygame.Rect(down_rect_loc[i],side_length)
                pygame.draw.rect(self.model.screen,self.model.player_colors[i],down_button,0)
                up_button = pygame.Rect((down_rect_loc[i][0],down_rect_loc[i][1]-(side_length[0]+10)),side_length)
                pygame.draw.rect(self.model.screen,self.model.player_colors[i],up_button,0)
                left_button = pygame.Rect((down_rect_loc[i][0]-(side_length[0]+10),down_rect_loc[i][1]),side_length)
                pygame.draw.rect(self.model.screen,self.model.player_colors[i],left_button,0)
                right_button = pygame.Rect((down_rect_loc[i][0]+(side_length[0]+10),down_rect_loc[i][1]),side_length)
                pygame.draw.rect(self.model.screen,self.model.player_colors[i],right_button,0)
                down_symbol = self.small_font.render(control_keys[i][0],1,self.black)
                down_loc = (int((side_length[0]-self.small_font.size(control_keys[i][0])[0])/2+down_rect_loc[i][0]),down_rect_loc[i][1])
                self.model.screen.blit(down_symbol,down_loc)
        controls_loc = (int((self.model.width-self.font.size("Player Controls")[0])/2),10)
        loading_loc = (int((self.model.width-self.font.size("Loading...")[0])/2),420)
        self.model.screen.blit(controls,controls_loc)
        self.model.screen.blit(loading,loading_loc)
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
