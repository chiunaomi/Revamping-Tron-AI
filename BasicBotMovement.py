from player import*
from tronmodel_bot import*
#argument that takes the position of the other player and takes it into consideration
#input single numbers into the functions as much as possible
#do the end game work in the model class
#self.player2.x for example as an argument
#abstract end game and crash from player and tronmodel as much as possible
class BasicBot(Player):
    def __init__(self, draw_screen, dimension, start_posx, start_posy, direction, color=(255,255,255)):
        Player.__init__(self, draw_screen, dimension, start_posx, start_posy, direction, color=(255,255,255))

    def random_choice_move(self, screen_height, screen_width):
    #def update(self):
        directions = ["r", "l", "u", "d"]
        safe = directions
        #head = TronModel.in_cell(self)
        self.px = 0
        self.py = 0
        #print(px,py)



        for d in range(4):
            self.dir = directions[d]
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
            self.x += self.vx
            self.y += self.vy
            possible_head = Rect(self.x, self.y, 10, 10)
            #print(px,py)
            if self.has_collided(self, other_player, possible_head, screen_width, screen_height): #or, then a function that checks whether the players have crashed
                safe.remove(self.dir)

        if self.dir not in safe and safe != []:
            self.dir = random.choice(safe)
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
            self.x += self.vx
            self.y += self.vy

        self.move()
    def has_collided(self, other_player, head = None, screen_width, screen_height):
        #figure out how to call the player paths from model, and call its own
        segments_to_check = TronModel.update.self.player_paths()
        head_loc = head.topleft
        return (not (0 <= head_loc[0] <= screen_width - 10) or
                not (0 <= head_loc[1] <= screen_height - 10) or
                head.collidelist(segments_to_check) != -1 or
                head.collidelist(other_player) != -1)
                #the above needs the input that checks the other players path from model
    def move(self):
        #need to grab current position below*** should try to grab it as a rect?
        #Just need top left into to implement though
        head_loc =
        delta = #state direction here
        new_x = head_loc[0] + delta['x'] * 10 #basially delta x should be either 0, 1, -1
        new_y = head_loc[1] + delta['y'] * 10 #delta y should be either 0, 1, -1
        newhead = Rect(new_x, new_y, 10, 10)
        self.player_path.insert(0, newhead)
        #the above code
"""
class Heuristic(self):
    def simple_heuristic(self):
        player_safe_count = BasicBot.random_choice_move(self)
        player_safe_count = len(player_safe_count)
        if player_safe_count == 0:
            return -1
        else:
            return 1
        return (4 - player_safe_count) / 3.0

class MinimaxBot(Player):
     This bot uses the well-known Minimax algorithm for its strategy,
    along with alpha-beta pruning to remove suboptimal branches.
    We use the following heuristic function to evaluate states:
    <To be done>
    For the leaves of the game tree, we consider win states to be 1
    and losses to be -1.


    def __init__(self, color, player_num, pruning=True, depth=1, heuristic=0):
        BasicBot(self, draw_screen, dimension, start_posx, start_posy, direction, color=(255,255,255))
        self.heuristic = heuristic
        self.pruning = pruning
        self.max_depth = depth # Max depth to explore for game tree

    def choose_move(self, other_player):
        self.set_direction(self.minimax(other_player, 0))
        self.move()

    def evaluate_board(self, player, turn):
        player_lost = Player.crash(self) or Tronmodel.end_game(self)
        #opponent_lost = opponent.has_collided(player)
        if (turn == 1):
            if player_lost:
                return -1
            else:
                return 1
        #if (turn == OPPONENT):
        #    if opponent_lost:
        #        return WIN
        #    if player_lost:
        #        return LOSE

        if self.heuristic == 0:
            return Heuristic.simple_heuristic(self)



        raise Exception("Heuristic Not Implemented")

    def minimax(self, depth):
        #print "Minimaxing for player#" + str(self.player_num)
        start_timer = timeit.default_timer()
        scores = [-1]*4
        moves = ["u","d","l","r"]
        random.shuffle(moves)
        max_score = -1
        for move in moves:
            if not self.direction_valid(move):
                continue
            scores[move] = self.min_play(self.clone(direction=move), depth+1, max_score, 1)
            max_score = max(max_score, scores[move])
            if self.pruning and max_score >= 1:
                break
        total_time = timeit.default_timer() - start_timer
        #print total_time
        #ret = scores.index(max(scores))
        #print "chose from: " + str(scores)
        return scores.index(max(scores)) # Move with highest score

    #def min_play(self, player, opponent, depth, alpha, beta):
    #    outcome = self.evaluate_board(player, opponent, OPPONENT)
    #    if outcome == 1 or outcome == -1 or depth == self.max_depth:
    #        return outcome
    #    min_score = 1
    #    for move in range(4):
    #        if not opponent.direction_valid(move):
    #            continue
    #        cloned_opponent = self.clone(player=opponent, direction=move)
    #        cur_val = self.max_play(player, cloned_opponent, depth+1, alpha, beta)
    #        min_score = min(cur_val, min_score)
    #        beta = min(beta, min_score)
    #        if self.pruning and beta <= alpha:
    #            break
    #        if min_score == 1:
    #            return 1
    #    return min_score

    #def max_play(self, player, opponent, depth, alpha, beta):
    #    outcome = self.evaluate_board(player, opponent, FRIENDLY)
    #    if outcome == 1 or outcome == -1 or depth == self.max_depth:
    #        return outcome
    #
    #    max_score = -1
    #    for move in range(4):
    #        if (not player.direction_valid(move)):
    #            continue
    #        cloned_player = self.clone(player=player, direction=move)
    #        cur_val = self.min_play(cloned_player, opponent, depth+1, alpha, beta)
    #        max_score = max(cur_val, max_score)
    #        alpha = max(max_score, alpha)
    #        if self.pruning and beta <= alpha:
    #            break
    #        if max_score == 1:
    #            return 1
    #    return max_score
"""
