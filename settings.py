import pygame
# settings.py
pygame.font.init()
pygame.init()



# Get the desktop resolution after initializing Pygame
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Guardian of the Presents")
clock = pygame.time.Clock()
FONT = pygame.font.Font(None, 36)
font = pygame.font.Font("assets/font/PixelatedEleganceRegular-ovyAA.ttf", 42)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
RED_TRANS = (255, 0 ,0, 0)
GREEN = (0, 255, 0)


# Player settings
player_width = 50
player_height = 50
player_speed = 5
player_velocity_x = 0
player_velocity_y = 0

# Bullet settings
bullet_width = 10
bullet_height = 10
refil_speed = 100
bullets = []
shield_boom = 0
# Enemy settings
enemy_width = 50
enemy_height = 50
enemy_speed = 3
enemies = []