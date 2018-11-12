import pygame
from pygame.locals import *

def timerFunc():
    print ("2 second desu")


def timerFunc2():
    print ("iTS ONE second")

pygame.init()
pygame.time.set_timer(USEREVENT+1, 1000)
pygame.time.set_timer(USEREVENT+2, 2000)

play =True
while (play == True):
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == USEREVENT+2:
            timerFunc2() #calling the function wheever we get timer event.
        if event.type == USEREVENT+1:
            timerFunc()
        if event.type == QUIT:
            play = False

        if keys[pygame.K_ESCAPE]:
            play = False