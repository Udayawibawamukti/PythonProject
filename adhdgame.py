import pygame
from pygame.locals import *
from random import randint

pygame.init()
pygame.font.init()
win=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption("ADHD FOCUST")

def atasDecay():
    kotakAtas.hitpoint = kotakAtas.hitpoint-5

def bawahDecay():
    kotakbawah.hitpoint = kotakbawah.hitpoint - 5

def summoner(temp):
    if temp == 0:
        kotakAtas.hitpoint = 500
        kotakAtas.visible = True
    if temp == 1:
        kotakbawah.hitpoint = 500
        kotakbawah.visible = True

def rect_bord(plat,color,sp):
    pygame.draw.rect(plat,(color.r,color.g,color.b),(sp.x,sp.y,sp.w,sp.h))
    pygame.draw.rect(plat,(0,0,0),(sp.x+5,sp.y+5,sp.w-10,sp.h-10))

def textCreate(text_in,color,sp):
    myfont = pygame.font.SysFont('Comic Sans MS', sp.w)
    texttemp = myfont.render(text_in, False, (color.r,color.g,color.b))
    win.blit(texttemp,(sp.x,sp.y))

def redrawGameWindow(sc):
    win.fill((0,0,0))
    textCreate(str(sc),Color(255,255,255),SP(0,0,20,0))
    kotakAtas.draw(win)
    kotakbawah.draw(win)
    user.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


class Color (object):
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b


class SP(object):
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

class playerCircle(object):
    def __init__(self,x,y,radius):
        self.x=int(x/2)
        self.y=int(y/2)
        self.radius=radius

    def draw(self,win):
        pygame.draw.circle(win, (255, 255, 255), (self.x, self.y), self.radius)

class enemiesSquare(object):
    def __init__(self,xkotak,ykotak,l_kotak,t_kotak,position,hitpoint):
        self.l_kotak=l_kotak/10*(lebar/16/5)
        self.t_kotak=t_kotak/10*(tinggi/9/5)
        self.position=position
        self.xkotak=(xkotak-self.l_kotak)/2
        self.ykotak=(ykotak/2)+(position*(ykotak/4))-(self.t_kotak/2)
        self.visible = True
        self.hitpoint = hitpoint
        self.hitbox = (self.xkotak, self.ykotak,self.l_kotak, self.t_kotak)

    def draw(self,win):
        if self.visible:
            rect_bord(win, Color(255, 255, 255), SP(self.xkotak, self.ykotak, self.l_kotak, self.t_kotak))
            self.hitbox = (self.xkotak-2, self.ykotak-2, self.l_kotak+5, self.t_kotak+5)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        if self.hitpoint<=0:
            self.visible = False

    def hit(self):
        print("hit!")



class projectiles(object):
    def __init__(self,x,y,radius,color,facing):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.facing=facing
        self.velocity=2*facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


lebar, tinggi = pygame.display.get_surface().get_size()
wplier, hplier = 16 / 5, 9 / 5
bullets = []
user = playerCircle(lebar, tinggi, 20)
enemies = []
kotakAtas = enemiesSquare(lebar, tinggi, 200, 80, 1, 1000)
kotakbawah = enemiesSquare(lebar, tinggi, 200, 80, -1, 1000)

def gamePlay():

    score = 0
    pygame.time.set_timer(USEREVENT+1, 1)
    pygame.time.set_timer(USEREVENT+2, 1)
    pygame.time.set_timer(USEREVENT+3, 2000)
    play = True

    while play:
        keys = pygame.key.get_pressed()
        #pygame.time.delay(10)

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                play = False

            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_SPACE]:
                    bullets.append(projectiles(int(kotakAtas.xkotak*1.5),int(kotakAtas.ykotak-10),10,(255,255,255),1))
                    #kotakAtas.hitpoint = kotakAtas.hitpoint - 10000
            elif event.type == pygame.KEYUP:
                if keys[pygame.K_SPACE]:
                    bullets.append(projectiles(int(kotakAtas.xkotak*1.5),int(kotakAtas.ykotak-10),10,(0,0,0),1))
            if event.type == USEREVENT+3:
                summoner(randint(0,1))
                #score = format(round(float(pygame.time.get_ticks() / 1000), 1))
            if event.type == USEREVENT+1:
                atasDecay()
            if event.type == USEREVENT+2:
                bawahDecay()
        """
        if keys[pygame.K_SPACE]:
            if len(bullets)<=2:
                bullets.append(projectiles(lebar, tinggi, 10, (255, 255, 255), 1))
        """
        for bullet in bullets:
            if kotakAtas.xkotak <= bullet.x < kotakAtas.xkotak + kotakAtas.l_kotak:
                if kotakAtas.ykotak < bullet.y < kotakAtas.ykotak + kotakAtas.t_kotak:
                    if kotakAtas.visible == True:
                        kotakAtas.hitpoint = kotakAtas.hitpoint - 10000
                        kotakAtas.hit()
                        bullets.pop(bullets.index(bullet))
                        score = score+1

            if tinggi > bullet.y > 0:
                bullet.y += bullet.velocity
            else:
                bullets.pop(bullets.index(bullet))
        #score = format(round(float(pygame.time.get_ticks()/1000),1))
        if keys[pygame.K_ESCAPE]:
            play = False
        
        #print(lebar)
        redrawGameWindow(score)
        #print(kotakAtas.visible)

gamePlay()
pygame.quit()


