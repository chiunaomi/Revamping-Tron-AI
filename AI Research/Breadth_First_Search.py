"""
Breadth First Search

 - Implement to maximize possible snake length

Returns: R,L,U(up),D(down) strings to tell player where to go
Takes: gird state (with no-go areas)


make implementaiton of breadth first, don't worry about adding to game
"""
import collections

"""
#creates a simple grid, replace with game
class SimpleGraph:
    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        return self.edges[id]

example_graph = SimpleGraph()
example_graph.edges = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['A'],
    'D': ['E', 'A'],
    'E': ['B']
}


class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()
def bfs(graph, start):
    #actual alogrithm - send gird, gamestate, and player's location)
    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True

    while not frontier.empty():
        current = frontier.get() #gets next 'frontier'(verticie) from the queue
        for next in graph.neighbors(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True
bfs(example_graph, 'A')
"""
class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()
#######################################
"""basically what we already have - a grid with walls"""
from DFS_Placeholder_Grid import *
myGrid = SquareGrid(30,20)
myGrid.walls = DIAGRAM1_WALLS
"""makes a list of walls - same as areas already been to in tron"""
draw_grid(myGrid)

"""
from tronmodel import TronModel
model = TronModel(10,640,480) #cell size, screen dimension
grid = model.cell_lst
"""


"""
tron model self.cell_lst
 - list of all cell_s


"""



def bfs_grid(graph, start, goal):
    #actual alogrithm - send gird, gamestate, and player's location
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = True
    #cost_so_far = {}
    #cost_so_far[start] =
    cost_so_far = 0


    while not frontier.empty():
        current = frontier.get() #gets next 'frontier'(verticie) from the queue
        if current == goal:
            break
        for next in graph.neighbors(current):
            #new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in came_from:
                #cost_so_far[next] = new_cost
                frontier.put(next)
                came_from[next] = True
                cost_so_far +=1
    return came_from, cost_so_far

parents = bfs_grid(myGrid, (8,5), (17,10))
#draw_grid(myGrid, width = 2, point_to = parents, start = (8,7))

draw_grid(myGrid, width = 2, number = parents, start = (8,5), goal=(17,10))

draw_grid(myGrid, width = 2, number = parents, start = (8,5), goal=(17,10))

#compute endx, endy from search to determine longest dist

"""
determine distance to each point
return coordinates of point for which max distance is traveled
use reconstruct_path to send commands to 'player' AI
"""




def reconstruct_path(came_from, start, goal): #should display path
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    #path.append(start) # optional
    #path.reverse() # optional
    return path

draw_grid(myGrid, width = 2, path = reconstruct_path(parents, start = (8,5), goal=(17,10)))


def get_path(grid, start, goal): #same as reconstruct_path
    came_from = bfs_grid(grid, start, goal)
    current = endspath = [goal]
    while not current ==start:
        current = came_from[current]
        path.append(current)
    return path.reverse()

get_path(parents, start = (8,5), goal=(17,2))
#draw_grid(myGrid, width = 2, path = get_path(parents, start = (8,5), goal=(17,2)))
