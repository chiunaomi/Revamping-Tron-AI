from player import*
from tronmodel import*

class BasicBot(Player):
    def __init__(self, draw_screen, dimension, start_posx, start_posy, direction, color=(255,255,255)):
        Player.__init__(self, draw_screen, dimension, start_posx, start_posy, direction, color=(255,255,255))

    def random_choice(self):
        possible_directions = range(4)
        directions= {"r", "l", "u", "d"}
        safe = possible_directions[:]
        head = TronModel.in_cell(self)


        for d in possible_directions:
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
            if self.crash or self.end_game:
                safe_directions.remove(direction)

        if self.direction not in safe_directions and safe_directions != []:
            self.direction = random.choice(safe_directions)

        self.move()

class Heuristic(self):
    def simple_heuristic(self):
        player_safe_count = random_choice(self)
        player_safe_count = len(player_safe_count)
        if player_safe_count == 0:
            return -1
        else:
            return 1
        return (4 - player_safe_count) / 3.0

class MinimaxBot(Player):
    """ This bot uses the well-known Minimax algorithm for its strategy,
    along with alpha-beta pruning to remove suboptimal branches.
    We use the following heuristic function to evaluate states:
    <To be done>
    For the leaves of the game tree, we consider win states to be 1
    and losses to be -1.
    """

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
