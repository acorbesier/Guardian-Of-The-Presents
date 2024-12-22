import pygame
from settings import *
import math

class RunGrinch(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, size=(64, 64)):
        super().__init__()

        # Load sprite images
        self.sprites = []
        for i in range(1, 15):  # Assuming there are 14 frames in the 'run' animation
            sprite_image = pygame.image.load(f'assets/images/grinch/run/run{i}.png')
            sprite_image = pygame.transform.scale(sprite_image, size)
            self.sprites.append(sprite_image)

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

        self.speed = 2  # Speed of the Grinch sprite
        self.flipped = False

    def update(self):
        # Update animation frame
        self.current_sprite += 1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        # Calculate the direction to the center of the screen
        center_x = screen_width // 2
        center_y = screen_height // 2

        dx = center_x - self.rect.centerx  # Difference in the x direction
        dy = center_y - self.rect.centery  # Difference in the y direction

        # Calculate the magnitude (length) of the vector to normalize
        magnitude = math.sqrt(dx**2 + dy**2)

        # Avoid division by zero (if magnitude is 0, meaning the Grinch is already at the center)
        if magnitude != 0:
            # Normalize the vector
            self.direction_x = dx / magnitude
            self.direction_y = dy / magnitude
        else:
            self.direction_x, self.direction_y = 0, 0

        # Update position based on direction
        self.rect.x += self.direction_x * self.speed
        self.rect.y += self.direction_y * self.speed

        # Determine if the sprite should be flipped based on direction
        if self.direction_x < 0 and not self.flipped:  # Moving right
            self.flipped = True
            self.sprites = [pygame.transform.flip(img, True, False) for img in self.sprites]
        elif self.direction_x > 0 and self.flipped:  # Moving left
            self.flipped = False
            self.sprites = [pygame.transform.flip(img, True, False) for img in self.sprites]
        
        # Update the current sprite image after flipping logic
        self.image = self.sprites[self.current_sprite]

        #Check if the Grinch has reached the center of the screen
        # if abs(self.rect.centerx - center_x) < 5 and abs(self.rect.centery - center_y) < 5:
        #     self.rect.center = (center_x, center_y)
        #     self.game_over()

    def game_over(self):
        global running, end_screen
        print("The Grinch reached the center! Game Over.")
        end_screen = True  # Trigger the end screen
        running = False  # Stop the game loop
