import pygame
from pygame.locals import *
from random import randint

pygame.init()
pygame.font.init()
win=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption("Menu Tes")
lebar, tinggi = pygame.display.get_surface().get_size()
hplier,wplier = (tinggi/9) / (768/9),(lebar/16)/(1366/16)

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

class Color():
    def __init__(self,r,g,b):
        self.r=r
        self.g = g
        self.b = b
class SP():
    def __init__(self,x,y,w,h):
        self.x=x #* wplier
        self.y = y#*hplier
        self.w = int(w*wplier)
        self.h = int(h*hplier)

class playerCircle(object):
    def __init__(self,x,y,radius):
        self.x=int(x/2)
        self.y=int(y/2)
        self.radius=radius

    def draw(self,win):
        pygame.draw.circle(win, (255, 255, 255), (self.x, self.y), self.radius)

class enemiesSquare(object):
    def __init__(self,xkotak,ykotak,l_kotak,t_kotak,position,hitpoint):
        self.l_kotak=l_kotak
        self.t_kotak=t_kotak
        self.position=position
        self.xkotak=(xkotak-self.l_kotak)/2
        self.ykotak=(ykotak/2)+(position*(ykotak/4))-(self.t_kotak/2)
        self.visible = True
        self.hitpoint = hitpoint
        self.hitbox = (self.xkotak, self.ykotak,self.l_kotak, self.t_kotak)

    def draw(self,win):
        if self.visible:
            rect_bord(win, Color(255, 255, 255), self.xkotak, self.ykotak,self.l_kotak, self.t_kotak)
            self.hitbox = (self.xkotak-2, self.ykotak-2, self.l_kotak+5, self.t_kotak+5)
            pygame.draw.rect(win, (0, 0, 0), self.hitbox, 2)
        if self.hitpoint<=0:
            self.visible = False

    def hit(self):
        print("hit!")

def textCreate(text_in,text_style,color,sp):
    myfont = pygame.font.Font(text_style, sp.w)
    texttemp = myfont.render(text_in, False, (color.r,color.g,color.b))
    text_width, text_height = myfont.size(text_in)
    win.blit(texttemp,(sp.x-text_width/2,sp.y-text_height/2))

def btnLoader(text_in,pathIdle,pathAct,scalex,scaley,posx,posy,action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    buttonidle = pygame.image.load(pathIdle)
    buttonact = pygame.image.load(pathAct)
    imgx, imgy = (buttonidle.get_rect().size)[0]* scalex *wplier,(buttonidle.get_rect().size)[1]* scaley*hplier
    myfont = pygame.font.Font('Asset\Campus A.ttf', int(0.45 * (imgx)/ 2))
    text_width, text_height = myfont.size(text_in)
    buttonimgidle = pygame.transform.scale(buttonidle, (int(imgx), int(imgy)))
    buttonimgact = pygame.transform.scale(buttonact, (int(imgx), int(imgy)))
    texttemp = myfont.render(text_in, False, (0, 0, 0))

    if posx-imgx/2<cur[0]<posx+imgx and posy-imgy/2<cur[1]<posy+imgy:
        win.blit(buttonimgact, (posx - (imgx / 2), posy - (imgy / 2)))
        if click[0] == 1 and action != None:
            if action == "start":
                print("button clicked")
                gamePlay()
            if action == "quit":
                pygame.quit()
                quit()
    else:
        win.blit(buttonimgidle, (posx - (imgx / 2), posy - (imgy / 2)))
        #pygame.draw.rect(win, (255, 0, 0), (posx-imgx/2, posy-imgy/2, posx+imgx, posy+imgy))
    win.blit(texttemp, (posx - text_width / 2, posy - text_height / 2))
    #print (imgx , imgy , text_width , text_height)

    #return buttonimg

def rect_bord(plat,color,x,y,w,h):
    pygame.draw.rect(plat,(color.r,color.g,color.b),(x,y,w,h))
    pygame.draw.rect(plat,(0,0,0),(x+5,y+5,w-10,h-10))

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

def redrawGameWindow(sc):
    win.fill((0,0,0))
    textCreate(str(sc),'Asset\Fine College.ttf',Color(255,255,255),SP(60,50,48,0))
    kotakAtas.draw(win)
    kotakbawah.draw(win)
    user.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


bullets = []
user = playerCircle(lebar, tinggi, 20)
enemies = []
kotakAtas = enemiesSquare(lebar, tinggi, 300, 150, 1, 1000)
kotakbawah = enemiesSquare(lebar, tinggi, 300, 150, -1, 1000)

def gameMenu():

    menu=True

    while menu:
        win.fill((255,255,255))
        keys = pygame.key.get_pressed()
        # pygame.time.delay(10)
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                menu = False

        btnLoader("Start","Asset\Button Idle.png","Asset\Button Act.png", 0.28, 0.18, lebar / 2-150, tinggi / 2+100, action="start")
        btnLoader("Quit","Asset\Button Idle.png","Asset\Button Act.png", 0.28, 0.18, lebar / 2+150, tinggi / 2+100, action="quit")

        textCreate("FOCUST", 'Asset\Fine College.ttf', Color(255, 0, 0), SP(lebar / 2, 250, 250, 0))
        pygame.display.update()


def gamePlay():
    score = 0
    pygame.time.set_timer(USEREVENT + 1, 1)
    pygame.time.set_timer(USEREVENT + 2, 1)
    pygame.time.set_timer(USEREVENT + 3, 2000)
    play = True

    while play:
        keys = pygame.key.get_pressed()
        # pygame.time.delay(10)

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                play = False

            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_SPACE]:
                    bullets.append(
                        projectiles(int(kotakAtas.xkotak*1.2), int(kotakAtas.ykotak - 10), 10, (0, 0, 0), 1))
                    # kotakAtas.hitpoint = kotakAtas.hitpoint - 10000
            elif event.type == pygame.KEYUP:
                if keys[pygame.K_SPACE]:
                    bullets.append(
                        projectiles(int(kotakAtas.xkotak*1.2), int(kotakAtas.ykotak - 10), 10, (0, 0, 0), 1))
            if event.type == USEREVENT + 3:
                summoner(randint(0, 1))
                # score = format(round(float(pygame.time.get_ticks() / 1000), 1))
            if event.type == USEREVENT + 1:
                atasDecay()
            if event.type == USEREVENT + 2:
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
                        score = score + 1

            if tinggi > bullet.y > 0:
                bullet.y += bullet.velocity
            else:
                bullets.pop(bullets.index(bullet))
        # score = format(round(float(pygame.time.get_ticks()/1000),1))
        if keys[pygame.K_ESCAPE]:
            gameMenu()

        # print(lebar)
        redrawGameWindow(score)
        # print(kotakAtas.visible)


gameMenu()
pygame.quit()
