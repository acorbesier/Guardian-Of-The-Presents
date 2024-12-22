import pygame
import sys
from settings import *
pygame.init()
info = pygame.display.Info()
X = info.current_w
Y = info.current_h

def book():
    screen = pygame.display.set_mode((X, Y), pygame.FULLSCREEN) 
    background = pygame.Surface((X, Y))  
    home_menu = pygame.image.load('assets/images/home.png')
    font = pygame.font.SysFont('Arial', 25)
    timer = pygame.time.Clock()
    book_foto1= pygame.image.load('scroll.png')
    book_foto2=pygame.image.load('scroll.png')
    book_x1 = X * -0.62
    book_y1 = Y * -0.05
    book_x2= X* 0.93
    book_y2= Y* -0.05


    
    messages = ["This is a quick little guide\nHow does one like you play our game?\nFirst I will go over ALLLL the controls:\nFundamentals are WASD or ZQSD Z or W meaning forward, A or Q going left, D going right and S being backwards\nOof that was a lot for one sentence\nLet us go over the interacts:\nReload happens with 'R', to interact with the shop press 'E' in the red square.\nLet's talk ingame statistics: there is a small chance to get a power-up each time a grinch is killed.\nThere are 3 power-ups 'Double coins', Unlimited 'Ammo' and 'Reindeer Nuke'.\nNot going to make this toooooo long and boring why don't you go out and try it for uself!\nGoodluck"]

    snip = font.render('', True, 'black')
    counter = 0
    speed = 4
    done = False
    active_message = 0
    message = messages[active_message]

    run = True
    while run:
        screen.fill(pygame.Color(255, 221, 138))
        timer.tick(60)
        
        
        if counter <= speed * len(message):
            counter += 1
        elif counter >= speed * len(message):
            done = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done and active_message < len(messages) - 1:        #loopt door main text door telkens & af te halen van main text en bij te tellen bij actieve text als ze gelijk zijn stopt het
                    active_message += 1
                    done = False
                    message = messages[active_message]
                    counter = 0
                elif event.key == pygame.K_RETURN and done and active_message == len(messages) - 1:
                    run = False 

        class Button: 
            def __init__(self, x, y, image, scale):
                self.original_image = image
                self.scale = scale
                self.hover_scale = scale * 1.1
                self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))       #exact zelfde code als start_screen button
                self.rect = self.image.get_rect()
                self.rect.topleft = (x, y)
                self.clicked = False

            def draw(self):
                action = False
                pos = pygame.mouse.get_pos()

                if self.rect.collidepoint(pos):
                    scaled_image = pygame.transform.scale(self.original_image, 
                                                    (int(self.original_image.get_width() * self.hover_scale),
                                                    int(self.original_image.get_height() * self.hover_scale)))
                    hover_rect = scaled_image.get_rect(center=self.rect.center)
                    screen.blit(scaled_image, hover_rect.topleft)
                else:
                    screen.blit(self.image, (self.rect.x, self.rect.y))

                if self.rect.collidepoint(pos):
                    if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                        self.clicked = True
                        action = True
                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False

                return action 
        class NotScaleButton: 
            def __init__(self, x, y, image, scale):
                self.original_image = image
                self.scale = scale
                self.hover_scale = scale 
                self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
                self.rect = self.image.get_rect()
                self.rect.topleft = (x, y)
                self.clicked = False

            def draw(self):
                action = False
                pos = pygame.mouse.get_pos()

                if self.rect.collidepoint(pos):
                    scaled_image = pygame.transform.scale(self.original_image, 
                                                    (int(self.original_image.get_width() * self.hover_scale),   #vrij nutteloos , exact zelfde code als hierboven aleen geen hover scale
                                                    int(self.original_image.get_height() * self.hover_scale)))
                    hover_rect = scaled_image.get_rect(center=self.rect.center)
                    screen.blit(scaled_image, hover_rect.topleft)
                else:
                    screen.blit(self.image, (self.rect.x, self.rect.y))

                if self.rect.collidepoint(pos):
                    if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                        self.clicked = True
                        action = True
                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False
        snip = font.render(message[0:counter // speed], True, 'black')
        screen.blit(snip, (100, 310))           #text placement
        home_knop = Button(X-(1/5)*X, Y-((1/9)*Y), home_menu, 0.351)
        book1 = NotScaleButton(book_x1, book_y1, book_foto1, 0.88)   
        book1.draw()
        book2=NotScaleButton(book_x2,book_y2,book_foto2,0.88)
        book2.draw()
    
        if home_knop.draw():
            run = False

        pygame.display.flip()
