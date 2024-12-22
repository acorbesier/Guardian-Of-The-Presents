import pygame
from settings import *

screen = pygame.display.set_mode((600, 800))
def draw_weapon(bullet_speed, player_x, player_y, player_velocity_x, last_direction):
    global path
    path = "assets/images/weapons//01 - Individual sprites/Guns/Glock - P80 [64x48].png"
    if bullet_speed == 13:
        path = "assets/images/weapons//01 - Individual sprites/Guns/Revolver - Colt 45 [64x32].png"
    if bullet_speed == 10:
        path = "assets/images/weapons//01 - Individual sprites/Guns/Glock - P80 [64x48].png"
    if bullet_speed == 15:
        path = "assets/images/weapons//01 - Individual sprites/Guns/Submachine - MP5A3 [80x48].png"
    if bullet_speed == 20:
        path = "assets/images/weapons/PNG/[design]Shotgun_V1.02.png"
    if bullet_speed == 25:
        path = "assets/images/weapons/01 - Individual sprites/Guns/AK 47 [96x48].png"
    if bullet_speed == 30:
        path = "assets/images/weapons/PNG/[design] Assault_rifle_V1.00.png"
    if bullet_speed == 35:
        path = "assets/images/weapons/PNG/[NO_BOLT]_Sniper_rifle_[KAR98]_V1.00.png"
    if bullet_speed == 40:
        path = "assets/images/weapons/PNG/[design]_Sniper_rifle_[KAR98]_V1.00.png"
    if player_velocity_x > 0 or last_direction > 0:
        if bullet_speed == 13 or bullet_speed == 10:
            gun_image = pygame.image.load(path)
            screen.blit(gun_image, (player_x + screen_width/60, player_y + screen_height/30))
        else:
            gun_image = pygame.image.load(path)
            screen.blit(gun_image, (player_x + screen_width/75, player_y + screen_height/30))
    else:
        if bullet_speed == 13 or bullet_speed == 10:
            gun_image = pygame.image.load(path)
            gun_image = pygame.transform.flip(gun_image, True, False)
            screen.blit(gun_image, (player_x - screen_width/60, player_y + screen_height/30))
        else:
            gun_image = pygame.image.load(path)
            gun_image = pygame.transform.flip(gun_image, True, False)
            screen.blit(gun_image, (player_x - screen_width/19, player_y + screen_height/30))