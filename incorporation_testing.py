import pygame
from pygame.locals import*
import os
from cell import Cell

pygame.init()
node = (range(20, 30),range(60,70))
def next_to(node):
    left = (range(node[0][0]-10,node[0][9]-9),node[1])
    right = (range(node[0][0]+10,node[0][9]+11),node[1])
    top = (node[0],range(node[1][0]+10,node[1][9]+11))
    bottom = (node[0],range(node[1][0]-10,node[1][9]-9))
    print(left)
    print(right)
    print(top)
    print(bottom)

next_to(node)

tron_font = pygame.font.Font(os.path.join(os.path.dirname(os.path.realpath(__file__)),'TRON.TTF'), 25)
print(640-tron_font.size("Loading...")[0])

screen = pygame.display.set_mode((640,480))
running = True
while running:
    side_length = (40,40)
    rectangle = pygame.Rect((300,200),side_length)
    rectangle1 = pygame.Rect((250,200),side_length)
    rectangle2 = pygame.Rect((350,200),side_length)
    rectangle3 = pygame.Rect((300,150),side_length)
    pygame.draw.rect(screen,(255,255,255),rectangle,0)
    pygame.draw.rect(screen,(255,255,255),rectangle1,0)
    pygame.draw.rect(screen,(255,255,255),rectangle2,0)
    pygame.draw.rect(screen,(255,255,255),rectangle3,0)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
pygame.quit()
