import pygame, sys
from pygame.locals import *

# initialize pygame module
pygame.init() 
DISPLAYSURF = pygame.display.set_mode((400, 300)) # screen size 400, 300 (width, height)
pygame.display.set_caption('Hello, GitHub!') # title of the window

while True:
    for event in pygame.event.get():
        print(event.type) # returns integer, for event type
        # QUIT is 12 
        # check print(pygame.locals.QUIT)
        if event.type == 12:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    
