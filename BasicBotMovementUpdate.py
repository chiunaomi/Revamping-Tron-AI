from player import Player
import random
#argument that takes the position of the other player and takes it into consideration
#input single numbers into the functions as much as possible
#do the end game work in the model class
#self.player2.x for example as an argument
#abstract end game and crash from player and tronmodel as much as possible
class BasicBot(Player):
    def __init__(self, model, draw_screen, dimension, start_posx, start_posy, direction, color_name, color) :
        Player.__init__(self, draw_screen, dimension, start_posx, start_posy, direction, color_name, color)
        #reset it so the model outputs a new list and sends the list each time to the AI
        self.model = model
        self.cell = None
        self.direction1 = direction

    def random_choice_move(self):
        directions = ["r", "l", "u", "d"]
        safe = ["r", "l", "u", "d"]
        self.px = self.x
        self.py = self.y
        for d in range(4):
            direction = directions[d]
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
            self.px += self.vx
            self.py += self.vy
            possible_head = (self.px,self.py)
            if self.has_collided(possible_head):
                safe.remove(direction)
            if direction in safe:
                if not self.direction_valid(direction):
                    safe.remove(direction)
        #if direction not in safe and safe != []:
            #direction = random.choice(safe)
        choices = len(safe)
        choose = random.randint(0, choices - 1)
        self.dir = safe[choose]
        self.direction1 = self.dir
        self.update()

    def has_collided(self, head):
        for cell in self.model.cell_lst:
            if head[0] in cell[0] and head[1] in cell[1]:
                self.cell = cell
        if self.cell in self.model.player_paths:
            return True

    def direction_valid(self, direction):
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
