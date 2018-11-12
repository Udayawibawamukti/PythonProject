import pygame

pygame.init()
pygame.font.init()
win = pygame.display.set_mode((800, 600))#,pygame.FULLSCREEN)
pygame.display.set_caption("Menu Tes")
lebar, tinggi = pygame.display.get_surface().get_size()
hplier, wplier = (tinggi / 9) / (768 / 9), (lebar / 16) / (1366 / 16)
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)


class Color():
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b


class SP():
    def __init__(self, x, y, w, h):
        self.x = x  # * wplier
        self.y = y  # *hplier
        self.w = int(w * wplier)
        self.h = int(h * hplier)


def textCreate(text_in, text_style, color, sp):
    myfont = pygame.font.Font(text_style, sp.w)
    texttemp = myfont.render(text_in, False, (color.r, color.g, color.b))
    text_width, text_height = myfont.size(text_in)
    win.blit(texttemp, (sp.x - text_width / 2, sp.y - text_height / 2))


def btnLoader(text_in, pathIdle, pathAct, scalex, scaley, posx, posy, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    buttonidle = pygame.image.load(pathIdle)
    buttonact = pygame.image.load(pathAct)
    imgx, imgy = (buttonidle.get_rect().size)[0] * scalex * wplier, (buttonidle.get_rect().size)[1] * scaley * hplier
    myfont = pygame.font.Font('Asset\Campus A.ttf', int(0.45 * (imgx) / 2))
    text_width, text_height = myfont.size(text_in)
    buttonimgidle = pygame.transform.scale(buttonidle, (int(imgx), int(imgy)))
    buttonimgact = pygame.transform.scale(buttonact, (int(imgx), int(imgy)))
    texttemp = myfont.render(text_in, False, (0, 0, 0))

    if posx - imgx / 2 < cur[0] < posx + imgx and posy - imgy / 2 < cur[1] < posy + imgy:
        win.blit(buttonimgact, (posx - (imgx / 2), posy - (imgy / 2)))
        if click[0] == 1 and action != None:
            if action == "start":
                print("button clicked")
            if action == "quit":
                pygame.quit()
                quit()
    else:
        win.blit(buttonimgidle, (posx - (imgx / 2), posy - (imgy / 2)))
        # pygame.draw.rect(win, (255, 0, 0), (posx-imgx/2, posy-imgy/2, posx+imgx, posy+imgy))
    win.blit(texttemp, (posx - text_width / 2, posy - text_height / 2))
    # print (imgx , imgy , text_width , text_height)

    # return buttonimg


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x-(w/2), y-(h/2), w, h)
        self.color = (150,50,50)
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = (0,0,255) if self.active else (150,50,50)
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


def addAcount():
    input_Name = InputBox(lebar/2, tinggi/2-100, 140, 32)
    input_Birth = InputBox(lebar / 2, tinggi / 2 - 50, 140, 32)
    input_boxes = [input_Name,input_Birth]
    add = True

    while add:
        win.fill((255, 255, 255))
        keys = pygame.key.get_pressed()
        # pygame.time.delay(10)
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                add = False
            if keys[pygame.K_ESCAPE]:
                add = False
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(win)

        btnLoader("Back", "Asset\Button Idle.png", "Asset\Button Act.png", 0.28, 0.18, lebar / 2 - 150,
                  tinggi / 2 + 100, action="start")
        btnLoader("Add", "Asset\Button Idle.png", "Asset\Button Act.png", 0.28, 0.18, lebar / 2 + 150, tinggi / 2 + 100,
                  action="quit")

        textCreate("add new account", 'Asset\Fine College.ttf', Color(255, 0, 0), SP(lebar / 2, 80, 100, 0))
        #textCreate("Please input second from 0.5 to 2 seconds", None, COLOR_INACTIVE, SP(lebar / 2, tinggi / 2-120, 48, 0))
        #textCreate("Default is 1 second", None, COLOR_INACTIVE,
        #           SP(lebar / 2, tinggi / 2+10, 48, 0))
        textCreate("Name                  :", None, Color(255,0,0), SP(lebar/2-150,tinggi/2-100,48,0))
        textCreate("Birthday Date   :", None, Color(255, 0, 0), SP(lebar / 2 - 150, tinggi / 2 - 50, 48, 0))
        pygame.display.update()


addAcount()
