"""
Breadth First Search

 - Implement to maximize possible snake length

Returns: R,L,U(up),D(down) strings to tell player where to go
Takes: gird state (with no-go areas)


make implementaiton of breadth first, don't worry about adding to game
"""


class SimpleGraph: """creates a simple grid, replace with game"""
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

import collections

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

#######################################

class SquareGrid: """basically what we already have"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results
