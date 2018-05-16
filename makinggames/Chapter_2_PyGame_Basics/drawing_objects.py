from pygame.locals import *
import pygame, sys

pygame.init()
DISPLAYSURF    = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Drawing")


BLACK = (0   ,     0,      0, 50)
WHITE = (255 ,   255,    255, 50)
RED   = (255 ,     0,      0, 50)
GREEN = (0   ,   255,      0, 50)
BLUE  = (0   ,     0,    255, 50)

DISPLAYSURF.fill(BLUE) # fill screen with blue 
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.line(DISPLAYSURF, WHITE, (60, 60),  (120, 60), 4)
pygame.draw.line(DISPLAYSURF, WHITE, (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, WHITE,  (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAYSURF, WHITE, (300, 50), 20, 0)
pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

while True:
    for event in pygame.event.get():
        print(event)
        if(event.type == QUIT):
            sys.exit()
    pygame.display.update()
