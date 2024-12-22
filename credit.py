import pygame
import sys

info=pygame.display.Info()
X=info.current_w
Y=info.current_h
def credit():

    pygame.init()

    info = pygame.display.Info()
    WIDTH = info.current_w   #relatieve schermgrootte 
    HEIGHT = info.current_h

    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Game Credits")

    
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    
    font = pygame.font.Font(None, 36)
    foto_home= pygame.image.load('assets/images/home.png')

    
    credits = [
        "Game Credits",
        "",
        "Developed by:",
        "Arthur Corbesier",
        "Cas Timmermans",
        "Seppe Huenaerts",
        "Milan de Proost",
        "Cyril Thonnard",
        "",
        "Credits:",
        "Fablefly Music", 
        "andres.notebook",
        "MurphysDad",
        "Kento Games", 
        "trashbait",
        "",
        "Music by:",
        "Fablefly Music,"
        "",
        "Thank you for playing!",
    ]

    
    rendered_text = [font.render(line, True, WHITE) for line in credits]

    #
    start_y = HEIGHT

    
    SCROLL_SPEED = 1

    #
    LINE_SPACING = 50

    
    clock = pygame.time.Clock()
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

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        
        y = start_y
        for text_surface in rendered_text:
            text_rect = text_surface.get_rect(center=(WIDTH // 2, y))
            screen.blit(text_surface, text_rect)
            y += LINE_SPACING  

        start_y -= SCROLL_SPEED

        
        if y < 0:
            start_y = HEIGHT
            
        home_knop=Button(X/1.1,Y/20,foto_home,0.351)

        if home_knop.draw():
            running = False
        
        pygame.display.flip()

        
        clock.tick(60)

    