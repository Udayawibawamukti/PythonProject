import pygame
pygame.init()
pygame.font.init()
win=pygame.display.set_mode((800,600))#,pygame.FULLSCREEN)
pygame.display.set_caption("Menu Tes")
lebar, tinggi = pygame.display.get_surface().get_size()
hplier,wplier = (tinggi/9) / (768/9),(lebar/16)/(1366/16)


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
            if action == "quit":
                pygame.quit()
                quit()
    else:
        win.blit(buttonimgidle, (posx - (imgx / 2), posy - (imgy / 2)))
        #pygame.draw.rect(win, (255, 0, 0), (posx-imgx/2, posy-imgy/2, posx+imgx, posy+imgy))
    win.blit(texttemp, (posx - text_width / 2, posy - text_height / 2))
    #print (imgx , imgy , text_width , text_height)

    #return buttonimg


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
            if keys[pygame.K_ESCAPE]:
                menu = False

        btnLoader("Start","Asset\Button Idle.png","Asset\Button Act.png", 0.28, 0.18, lebar / 2-150, tinggi / 2+100, action="start")
        btnLoader("Quit","Asset\Button Idle.png","Asset\Button Act.png", 0.28, 0.18, lebar / 2+150, tinggi / 2+100, action="quit")

        textCreate("FOCUST", 'Asset\Fine College.ttf', Color(255, 0, 0), SP(lebar / 2, 250, 250, 0))
        pygame.display.update()

gameMenu()
