import pygame

class IdleSanta(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, size=(64, 64), animation_speed=4):  
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/images/santa/Idle/idle1.png'), size))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/images/santa/Idle/idle2.png'), size))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/images/santa/Idle/idle3.png'), size))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/images/santa/Idle/idle4.png'), size))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/images/santa/Idle/idle5.png'), size))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/images/santa/Idle/idle6.png'), size))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.animation_speed = animation_speed  
        self.animation_counter = 0  

        
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.direction_x = 0
        self.flipped = False

    def update(self):
        self.animation_counter += 1

        if self.animation_counter >= self.animation_speed:
            self.animation_counter = 0 
            self.current_sprite += 1

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
            
            self.image = self.sprites[self.current_sprite]
        
        if self.direction_x == -1:
            self.image = pygame.transform.flip(self.image, True, False)  # Spiegel horizontaal
        # elif self.direction_x == 1:
        #     self.image = pygame.transform.flip(self.image, False, False)  # Geen flip

        if self.direction_x < 0 and not self.flipped:  # Moving right
            self.flipped = True
            self.sprites = [pygame.transform.flip(img, True, False) for img in self.sprites]
        elif self.direction_x > 0 and self.flipped:  # Moving left
            self.flipped = False
            self.sprites = [pygame.transform.flip(img, True, False) for img in self.sprites]
        
        # Update the current sprite image after flipping logic
        self.image = self.sprites[self.current_sprite]



    
class RunSanta(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, size=(64, 64), animation_speed=3):  
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/images/santa/run/run1.png'), size))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/images/santa/run/run2.png'), size))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/images/santa/run/run3.png'), size))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/images/santa/run/run4.png'), size))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/images/santa/run/run5.png'), size))
        self.sprites.append(pygame.transform.scale(pygame.image.load('assets/images/santa/run/run6.png'), size))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.animation_speed = animation_speed
        self.animation_counter = 0

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

        self.flipped = False
        self.direction_x = 0
    
    def update(self):
        self.animation_counter += 1

        if self.animation_counter >= self.animation_speed:
            self.animation_counter = 0
            self.current_sprite += 1

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
            
            self.image = self.sprites[self.current_sprite]
        
        # Determine if the sprite should be flipped based on direction
        if self.direction_x < 0 and not self.flipped:  # Moving right
            self.flipped = True
            self.sprites = [pygame.transform.flip(img, True, False) for img in self.sprites]
        elif self.direction_x > 0 and self.flipped:  # Moving left
            self.flipped = False
            self.sprites = [pygame.transform.flip(img, True, False) for img in self.sprites]
        
        # Update the current sprite image after flipping logic
        self.image = self.sprites[self.current_sprite]

