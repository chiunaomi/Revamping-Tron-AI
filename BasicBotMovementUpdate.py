"""
AI bot object that defines the behavior of the CPUs
"""
from player import Player
import random

class BasicBot(Player): #inherits player class' methods
    def __init__(self, model, draw_screen, dimension, start_posx, start_posy, direction, color_name, color):
        """initializes bot's location, direction, speed, color as well as the model that the bot uses to make decisions"""
        Player.__init__(self, draw_screen, dimension, start_posx, start_posy, direction, color_name, color)
        #reset it so the model outputs a new list and sends the list each time to the AI
        self.model = model
        self.cell = None
        self.direction1 = direction

    def random_choice_move(self):
        """performs a depth search to choose which direction to go in"""
        directions = ["r", "l", "u", "d"] #list of possible directions
        safe = ["r", "l", "u", "d"] #list of safe directions that will not result in a loss
        self.px = self.x #potential x position (not the actual) for the depth search
        self.py = self.y #potential y position (not the actual) for the depth search

        self.pseudo_update(self.dir) #updates potential position based on current direction
        next_head = (self.px,self.py)
        if self.has_collided(next_head): #checks to see if current direction will lead to a collision
            for d in range(4):
                self.px = self.x #reset potential x position to current x position
                self.py = self.y #reset potential y position to current y position
                direction = directions[d] #for each direction in possible directions
                if direction == "r":
                    self.vx = 10
                    self.vy = 0
                elif direction == "l":
                    self.vx = -10
                    self.vy = 0
                elif direction == "u":
                    self.vx = 0
                    self.vy = -10
                elif direction == "d":
                    self.vx = 0
                    self.vy = 10
                self.px += self.vx #update potential position
                self.py += self.vy
                possible_head = (self.px,self.py)
                if self.has_collided(possible_head): #check of direction will lead to collision
                    safe.remove(direction)
                if direction in safe:
                    if not self.direction_valid(direction): #checks to see if direction will cause bot to turn back on itself
                        safe.remove(direction)
            choices = len(safe)
            if choices != 0: #if there are still options in the safe directions
                choose = random.randint(0, choices - 1)
                dir = safe[choose] #choose a random direction
            else:
                dir = self.dir #if not, continue in its current direction as it will lose anyways
            self.dir = dir
            self.direction1 = self.dir
        self.update()

    def pseudo_update(self,direction):
        "updates potential position of the bot according to the direction given"
        if direction == "r":
            self.vx = 10
            self.vy = 0
        elif direction == "l":
            self.vx = -10
            self.vy = 0
        elif direction == "u":
            self.vx = 0
            self.vy = -10
        elif direction == "d":
            self.vx = 0
            self.vy = 10
        elif direction == "None":
            self.vx = 0
            self.vy = 0
        self.px += self.vx
        self.py += self.vy

    def has_collided(self, head):
        "checks its position with the list of already occupied cells from the model to check for collision"
        for cell in self.model.cell_lst:
            if head[0] in cell[0] and head[1] in cell[1]:
                self.cell = cell
        if self.cell in self.model.player_paths:
            return True

    def direction_valid(self, direction):
        "checks that the bot will not be reversing direction and driving into itself"
        if (direction == "u" and self.direction1 == "d"):
            return False
        if (direction == "l" and self.direction1 == "r"):
            return False
        if (direction == "d" and self.direction1 == "u"):
            return False
        if (direction == "r" and self.direction1 == "l"):
            return False
        else:
            return True
