"""
Entire code in one file for ease in editing how classes work together.
Edits made here are transferred into individual files for final code.
"""
import pygame
from pygame.locals import*
import time
import os

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
        self.num_players = None

    def init_players(self):
        "Initiates number of players specified by user input"
        if self.num_players == None:
            return
        if self.num_players == 1:
            self.player1 = Player(self.screen,10,(self.width/2-100),(self.height/2),"l",self.color_strings[0],self.player_colors[0])
            self.players = [self.player1]
        if self.num_players == 2:
            self.player1 = Player(self.screen,10,(self.width/2-100),(self.height/2),"l",self.color_strings[0],self.player_colors[0])
            self.player2 = Player(self.screen,10,(self.width/2+100),(self.height/2),"r",self.color_strings[1],self.player_colors[1])
            self.players = [self.player1,self.player2]
        if self.num_players == 3:
            self.player1 = Player(self.screen,10,(self.width/2-100),(self.height/2-50),"l",self.color_strings[0],self.player_colors[0])
            self.player2 = Player(self.screen,10,(self.width/2+100),(self.height/2-50),"r",self.color_strings[1],self.player_colors[1])
            self.player3 = Player(self.screen,10,(self.width/2-100),(self.height/2+50),"l",self.color_strings[2],self.player_colors[2])
            self.players = [self.player1,self.player2,self.player3]
        if self.num_players == 4:
            self.player1 = Player(self.screen,10,(self.width/2-100),(self.height/2-50),"l",self.color_strings[0],self.player_colors[0])
            self.player2 = Player(self.screen,10,(self.width/2+100),(self.height/2-50),"r",self.color_strings[1],self.player_colors[1])
            self.player3 = Player(self.screen,10,(self.width/2-100),(self.height/2+50),"l",self.color_strings[2],self.player_colors[2])
            self.player4 = Player(self.screen,10,(self.width/2+100),(self.height/2+50),"r",self.color_strings[3],self.player_colors[3])
            self.players = [self.player1,self.player2,self.player3,self.player4]
        if self.num_CPU == 1:
            print(1)
        if self.num_CPU == 2:
            print(2)

    def _draw_players(self):
        """Calls the player objects' draw functions"""
        for player in self.players:
            player.draw()

    def in_cell(self):
        """Loops through cell_lst to find the cell whose xrange contains player.x
        and whose yrange contains player.y, and sets the player location to be within that cell."""
        for player in self.players:
            for cell in self.cell_lst:
                if player.x in cell[0] and player.y in cell[1]:
                    player.current_cell = cell
                    break

    def update(self):
        """Checks for new inputs and updates the game model."""
        for player in self.players:
            player.update()
            player.last_seen = player.current_cell

        self.in_cell()
        for player in self.players:
            if player.current_cell != player.last_seen:
                self.player_paths.add(player.last_seen)
        #If the player has left a cell and moved into another, the vacated cell is
        #added to the list of cells that have been hit
            if player.current_cell in self.player_paths:
                self.players.remove(player)
                player.alive = False
        if len(self.players) == 1:
            self.end_game(self.players[0].name,self.players[0].color)

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

class Cell(object):
    """Cell object defining the visualized form of a cell.
    Not used structurally to define player locations, but used to visualize the game"""
    def __init__(self, draw_screen, coordinates, side_length):
        self.xrange = range(coordinates[0],coordinates[0]+side_length)
        self.yrange = range(coordinates[1],coordinates[1]+side_length)
        self.draw_screen = draw_screen
        self.coordinates = coordinates
        self.side_length = (side_length,side_length)
        self.color = (0, 0, 0)

    def draw(self):
        line_width = 1
        rect = pygame.Rect(self.coordinates, self.side_length)
        pygame.draw.rect(self.draw_screen, self.color, rect, line_width)

class Player(object):
    """Contains player's location, direction and speed, as well as their color"""
    def __init__(self, draw_screen, dimension, start_posx, start_posy, direction, color_name, color=(255,255,255)):
        self.draw_screen = draw_screen
        self.width = dimension
        self.height = dimension
        self.x = start_posx
        self.y = start_posy
        self.vx = 0
        self.vy = 0
        self.dir = direction
        self.color = color
        self.name = color_name
        self.last_seen = None
        self.current_cell = None
        self.alive = True

    def draw(self):
        line_width = .5
        pygame.draw.rect(self.draw_screen,self.color,pygame.Rect(self.x,self.y,self.width,self.height))

    def update(self):
        """Checks if players have changed directions, and then
        adds the correct number of pixels to the player's position in the relevant direction"""
        if self.dir == "r":
            self.vx = 10
            self.vy = 0
        elif self.dir == "l":
            self.vx = -10
            self.vy = 0
        elif self.dir == "u":
            self.vx = 0
            self.vy = -10
        elif self.dir == "d":
            self.vx = 0
            self.vy = 10
        elif self.dir == "None":
            self.vx = 0
            self.vy = 0
        self.x += self.vx
        self.y += self.vy

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
            end_mode_setup = False
            end_player_setup = False
            game_over = False

            while not end_start:
                view.start_screen()
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
                view.mode_setup()
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
                if model.mode == "single":
                    model.num_players = 1
                    view.single_player_setup()
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            running = False
                            end_player_setup = True
                            game_over = True
                        if controller.handle_single(event):
                            model.init_players()
                            controller.end_player_setup = True
                            end_player_setup = True
                if model.mode == "multi":
                    end_multi1 = False
                    while not end_multi1:
                        view.multi_player_setup1()
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
                                if model.num_players == 4:
                                    end_multi2 = True
                                else:
                                    end_multi2 = False
                    while not end_multi2:
                        view.multi_player_setup2()
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

            view._init_draw()
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
