import pygame
import pygame_gui
import random
import math
import sys
from settingscreen import settingscreen
from tutorial import tutorial
from pygame.locals import *
from book import book
from credit import credit
pygame.init()

pygame.mixer.init()



wave = pygame.mixer.Sound('assets/sounds/wave.mp3')


info = pygame.display.Info()
X = info.current_w   #relatieve schermgrootte 
Y = info.current_h
def draw_gradient(surface, color1, color2, width, height):
     for y in range(height): #loopt van boven naar beneden
        blend_ratio = y / height #hoeveel gemengd
        r = int(color1[0] * (1 - blend_ratio) + color2[0] * blend_ratio)           #kleur maken door blenden (niet zelf gemaakt chatgpt lol)
        g = int(color1[1] * (1 - blend_ratio) + color2[1] * blend_ratio)
        b = int(color1[2] * (1 - blend_ratio) + color2[2] * blend_ratio)
        pygame.draw.line(surface, (r, g, b), (0, y), (width, y))   #kleur_overgang dmv lijn
top_color = (51, 102, 255)  # #3366ff
bottom_color = (204, 255, 204)  # #ccffcc



white = (255, 255, 255) 
screen = pygame.display.set_mode((X, Y))
background = pygame.Surface((X, Y))          #achtergrond maken, kleur 
background.fill(pygame.Color(185, 195, 255))


manager = pygame_gui.UIManager((X, Y))
start_geluid = pygame.mixer.Sound('assets/sounds/rechamb.mp3')


start_foto = pygame.image.load('assets/images/start.png').convert_alpha()
quit_foto = pygame.image.load('assets/images/pngwing.com.png').convert_alpha()
logo_foto = pygame.image.load('assets/images/newlogo.png').convert_alpha()      #afbeeldingen inladen
settings_foto = pygame.image.load('assets/images/settings.png').convert_alpha()
tutorial_foto= pygame.image.load('assets/images/tutorial.png').convert_alpha()
book_foto=pygame.image.load('book.png').convert_alpha()
credits_foto=pygame.image.load('assets/images/credits.png').convert_alpha()


pygame.display.set_caption("Guardian of the present")

class Button: 
    def __init__(self, x, y, image, scale):
        self.original_image = image
        self.scale = scale *1   
        self.hover_scale = scale * 1.1          #vergroot gemaakt op klasse
        self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale))) #functionaliteit vergroting
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()  #muispositie 

        
        if self.rect.collidepoint(pos):
            scaled_image = pygame.transform.scale(self.original_image, (int(self.original_image.get_width() * self.hover_scale),
            int(self.original_image.get_height() * self.hover_scale))) #bij hover over knop doet vergroting
            hover_rect = scaled_image.get_rect(center=self.rect.center)
            screen.blit(scaled_image, hover_rect.topleft) #toont nieuwe weer
        else:
            screen.blit(self.image, (self.rect.x, self.rect.y)) #origineel zonder scale

        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True                                #klikt op het geselecteerde punt
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action
class Notscale:    #identiek dezelfde klasse als Button, maar scaalt niet
        def __init__(self, x, y, image, scale):
            self.original_image = image
            self.scale = scale *1
            self.hover_scale = scale * 1
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

start_knop = Button(X/2.85, Y/2.3, start_foto, 0.4)
quit_knop = Button(X/18, Y/20, quit_foto, 0.055)
logo = Notscale(X/4.5, Y/95, logo_foto, 0.8)                #geeft positie op scherm relatief weer, en past schaal aan
settings = Button(X/1.09, Y/1.2, settings_foto, 0.20)
tutorial_knop=Button(X/2.75,Y/1.25,tutorial_foto,0.4)
book_knop=Button(X/1.1,Y/1.5,book_foto,0.35)
credit_knop=Button(X/1.1,Y/2,credits_foto,0.25)

sneeuwvloks = []
for i in range(30): 
    sneeuwvloks.append({
        'x': random.randint(0, X),          #spawnt random in over het scherm, bovenaan
        'y': random.randint(-Y, 0),
        'speed': random.uniform(0.6, 0.8),  
        'size': random.randint(6, 10)  
    })

def draw_sneeuwvlok(surface, x, y, size):
    for angle in range(0, 360, 60):               #elke 60° een angle
        radians = math.radians(angle)             
        end_x = x + size * math.cos(radians)    #tekenen van hoeken van 60°
        end_y = y + size * math.sin(radians)
        pygame.draw.line(surface, white, (x, y), (end_x, end_y), 1)

        for branch_angle in (-25, 5):  
            branch_radians = math.radians(angle + branch_angle)
            branch_x = x + (size // 2) * math.cos(branch_radians)
            branch_y = y + (size // 2) * math.sin(branch_radians)
            pygame.draw.line(surface, white, (end_x, end_y), (branch_x, branch_y), 1)





clock = pygame.time.Clock()
angle=0


screen = pygame.display.set_mode((X, Y))
background = pygame.Surface((X, Y))


draw_gradient(background, top_color, bottom_color, X, Y)

def start_screen(wave, reload, noammo):
    global angle
    is_running = True

    terug_draaien = 1  # -1 klokslag tegen, 1 met klokslag mee
    aantal_graden = 5 #hoekgrootte van draaien

    while is_running:
        klokje_fps = clock.tick(20)
        angle += terug_draaien

        # Reverse rotation direction at max range
        if angle >= aantal_graden or angle <= -aantal_graden:
            terug_draaien *= -1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            manager.process_events(event)


        for sneeuwvlok in sneeuwvloks:
            sneeuwvlok['y'] += sneeuwvlok['speed']
            sneeuwvlok['x'] += random.uniform(-0.10, 0.18)
            if sneeuwvlok['y'] > Y:
                sneeuwvlok['y'] = random.randint(-5, 100)
                sneeuwvlok['x'] = random.randint(5, X)
                sneeuwvlok['speed'] = random.uniform(0.5, 2.5)

        screen.blit(background, (0, 0))

        for sneeuwvlok in sneeuwvloks:
            draw_sneeuwvlok(screen, sneeuwvlok['x'], sneeuwvlok['y'], sneeuwvlok['size'])

        if settings.draw():
            settingscreen(wave, reload, noammo)
        if book_knop.draw():
            book()
        if credit_knop.draw():
            credit()
        
        if quit_knop.draw():
            pygame.quit()
            sys.exit()

        if tutorial_knop.draw():
            tutorial()

        if start_knop.draw():
            start_geluid.play()
            is_running = False
            wave.play()

        rotated_logo = pygame.transform.rotate(logo_foto, angle)
        rotated_rect = rotated_logo.get_rect(center=(X // 2, Y // 7))  # Logo_positie
        screen.blit(rotated_logo, rotated_rect.topleft)

        manager.update(klokje_fps)
        manager.draw_ui(screen)

        pygame.display.update()
