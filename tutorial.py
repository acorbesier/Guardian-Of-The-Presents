import pygame
import sys
from settings import *
pygame.init()
info = pygame.display.Info()
X = info.current_w
Y = info.current_h

def tutorial():
    screen = pygame.display.set_mode((X, Y), pygame.FULLSCREEN) 
    background = pygame.Surface((X, Y))  
    home_menu = pygame.image.load('assets/images/home.png')
    font = pygame.font.SysFont('Arial', 25)
    timer = pygame.time.Clock()
    grinch_foto= pygame.image.load('assets/images/grinch/grinch.png')
    grinch_x = X * 0.5  
    grinch_y = Y * 0.4   


    
    messages = ['Hey Rookie!\nWelcome to the tutorial!\nPress Enter to continue', 
                'Movement goes with ZQSD.\nI am sure you are familiar with how these binds work right?\nIf not you can always change them in the settings.', 
                'Santa has been busy making presents, defend them!', 
                'For once in your life dont be a disappointment and do something useful.',
                'Collect coins and upgrade your pew pews.', 
                'Goodluck!\nGoOoOoOoooOo and save Christmas Rookie!',
                'Okay thats all you can press main menu now!\nBy pressing the Home icon on the bottom right.',
                'What did I tell you go to main menu now please!',
                'You have made it this far but dont go further.\nI have already told you to click the Home button.',
                'Hey I warned you stop it Rookie!\nDo not make me say it again!', 
                'Okay so you want to be stubborn?\nFine, but do not press enter one more F*#@!kng time!!!',
                'I will send you to the Home screen myself if I have to.',
                'Im being serious Rookie!']

    snip = font.render('', True, 'black')
    counter = 0
    speed = 2
    done = False
    active_message = 0
    message = messages[active_message]

    run = True
    while run:
        screen.fill(pygame.Color(185, 195, 255))
        timer.tick(60)
        pygame.draw.rect(screen, 'white', [0, 300, X, 250])
        
        if counter <= speed * len(message):
            counter += 1
        elif counter >= speed * len(message):
            done = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done and active_message < len(messages) - 1:
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
                self.hover_scale = scale * 1.15
                self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
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

        snip = font.render(message[0:counter // speed], True, 'black')
        screen.blit(snip, (10, 310))
        home_knop = Button(X-(1/14)*X, Y-((1/2.1)*Y), home_menu, 0.351)
        grinch = Button(grinch_x, grinch_y, grinch_foto, 0.38)   
        grinch.draw()
        if home_knop.draw():
            run = False

        pygame.display.flip()



