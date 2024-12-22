import pygame
from settings import *


pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

co_shop1 = (screen_width/ 3.11, screen_height/2.45)
co_shop2 = (screen_width/ 2.465, screen_height/2.45)
co_shop3 = (screen_width/ 2.05, screen_height/2.45)
co_shop4 = (screen_width/ 1.755, screen_height/2.45)
co_shop5 = (screen_width/ 1.534, screen_height/2.45)

co_shop6 = (screen_width/ 3.11, screen_height/1.9)
co_shop7 = (screen_width/ 2.465, screen_height/1.9)
co_shop8 = (screen_width/ 2.05, screen_height/1.9)
co_shop9 = (screen_width/ 1.755, screen_height/1.9)
co_shop10 = (screen_width/ 1.534, screen_height/1.9)

co_shop11 = (screen_width/ 3.11, screen_height/1.555)
co_shop12 = (screen_width/ 2.465, screen_height/1.555)
co_shop13 = (screen_width/ 2.05, screen_height/1.555)
co_shop14 = (screen_width/ 1.755, screen_height/1.555)
co_shop15 = (screen_width/ 1.534, screen_height/1.555)
shape = 50, 15


screen = pygame.display.set_mode((screen_width, screen_height ))

def draw_shopscreen():
    global shop1, shop2, shop3, shop4, shop5, shop6, shop7, shop8, shop9, shop10, shop11, shop12, shop13, shop14, shop15, shop_rect
    scale_width = screen_width / 800
    scale_height = screen_height / 600
    shop_image = pygame.image.load("assets/images/shop-front.png").convert_alpha()
    shop_width = shop_image.get_width()
    shop_height = shop_image.get_height()
    shop_image = pygame.transform.scale(shop_image, (shop_width  * 0.9 * scale_width , shop_height * 0.9 * scale_height))  
    screen.blit(shop_image, (screen_width/ 6.6, screen_height/ 6.5))
    

    shop_close_image = pygame.image.load("assets/images/knop_rood.png").convert_alpha()
    close_image_size = 80,80
    shop_close_image = pygame.transform.scale(shop_close_image, (close_image_size))   # kleiner maken
    close_image_location = (screen_width/ 1.4, screen_height/ 4.3)
    screen.blit(shop_close_image, (close_image_location))
    shop_rect = pygame.Rect((screen_width/ 1.3852, screen_height/ 4.15, 60, 60))
    
    # om te tekenen
    # shop_rect = pygame.draw.rect(screen, RED, (screen_width/ 1.3852, screen_height/ 4.15, 60, 60))

    shop1 = pygame.Rect(co_shop1, shape)
    shop2 = pygame.Rect(co_shop2, shape)
    shop3 = pygame.Rect(co_shop3, shape)
    shop4 = pygame.Rect(co_shop4, shape)
    shop5 = pygame.Rect(co_shop5, shape)
    shop6 = pygame.Rect(co_shop6, shape)
    shop7 = pygame.Rect(co_shop7, shape)
    shop8 = pygame.Rect(co_shop8, shape)
    shop9 = pygame.Rect(co_shop9, shape)
    shop10 = pygame.Rect(co_shop10, shape)
    shop11 = pygame.Rect(co_shop11, shape)
    shop12 = pygame.Rect(co_shop12, shape)
    shop13 = pygame.Rect(co_shop13, shape)
    shop14 = pygame.Rect(co_shop14, shape)
    shop15 = pygame.Rect(co_shop15, shape)


    # tekent de vakken om te plaatsen
    # shop1 = pygame.draw.rect(screen, RED, (co_shop1, shape))    
    # shop2 = pygame.draw.rect(screen, RED, (co_shop2, shape))
    # shop3 = pygame.draw.rect(screen, RED, (co_shop3, shape))
    # shop4 = pygame.draw.rect(screen, RED, (co_shop4, shape))
    # shop5 = pygame.draw.rect(screen, RED, (co_shop5, shape))
    # shop6 = pygame.draw.rect(screen, RED, (co_shop6, shape))
    # shop7 = pygame.draw.rect(screen, RED, (co_shop7, shape))
    # shop8 = pygame.draw.rect(screen, RED, (co_shop8, shape))
    # shop9 = pygame.draw.rect(screen, RED, (co_shop9, shape))
    # shop10 = pygame.draw.rect(screen, RED, (co_shop10, shape))
    # shop11 = pygame.draw.rect(screen, RED, (co_shop11, shape))
    # shop12 = pygame.draw.rect(screen, RED, (co_shop12, shape))
    # shop13 = pygame.draw.rect(screen, RED, (co_shop13, shape))
    # shop14 = pygame.draw.rect(screen, RED, (co_shop14, shape))
    # shop15 = pygame.draw.rect(screen, RED, (co_shop15, shape))


def shopscreen(score, bullet_speed, shield_boom, lives, bullet_amount, shots_fired):

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if shop1.collidepoint(event.pos):
                    if score >= 20:
                        pygame.mixer.Sound("assets/sounds/buy_1.mp3").play()
                        score -= 20
                        running = False
                    else:
                        pygame.mixer.Sound("assets/sounds/buzzer.wav").play()
                elif shop2.collidepoint(event.pos):
                    if score >= 30 and bullet_speed != 10:
                        bullet_amount = 12
                        lastbulletamount = 12
                        shots_fired = 0
                        bullet_speed = 10
                        pygame.mixer.Sound("assets/sounds/buy_1.mp3").play()
                        score -= 30
                        running = False
                    else:
                        pygame.mixer.Sound("assets/sounds/buzzer.wav").play()
                elif shop3.collidepoint(event.pos):
                    if score >= 40:
                        bullet_amount = 6
                        lastbulletamount = 6
                        shots_fired = 0
                        bullet_speed = 13
                        pygame.mixer.Sound("assets/sounds/buy_1.mp3").play()
                        score -= 40
                        running = False
                    else:
                        pygame.mixer.Sound("assets/sounds/buzzer.wav").play()
                elif shop4.collidepoint(event.pos):
                    if score >= 60:
                        bullet_amount = 26
                        lastbulletamount = 26
                        shots_fired = 0
                        bullet_speed = 15
                        pygame.mixer.Sound("assets/sounds/buy_1.mp3").play()
                        score -= 60
                        running = False
                    else:
                        pygame.mixer.Sound("assets/sounds/buzzer.wav").play()
                elif shop5.collidepoint(event.pos):
                    if score >= 60:
                        bullet_amount = 6
                        lastbulletamount = 6
                        shots_fired = 0
                        bullet_speed = 20
                        pygame.mixer.Sound("assets/sounds/buy_1.mp3").play()
                        score -= 60
                        running = False
                    else:
                        pygame.mixer.Sound("assets/sounds/buzzer.wav").play()
                elif shop6.collidepoint(event.pos):
                    if score >= 100:
                        bullet_amount = 30
                        lastbulletamount = 30
                        shots_fired = 0
                        bullet_speed = 25
                        pygame.mixer.Sound("assets/sounds/buy_1.mp3").play()
                        score -= 100
                        running = False
                    else:
                        pygame.mixer.Sound("assets/sounds/buzzer.wav").play()
                elif shop7.collidepoint(event.pos):
                    if score >= 150:
                        bullet_amount = 32
                        lastbulletamount = 32
                        shots_fired = 0
                        bullet_speed = 30
                        pygame.mixer.Sound("assets/sounds/buy_1.mp3").play()
                        score -= 150
                        running = False
                    else:
                        pygame.mixer.Sound("assets/sounds/buzzer.wav").play()
                elif shop8.collidepoint(event.pos):
                    if score >= 90:
                        bullet_amount = 3
                        lastbulletamount = 3
                        shots_fired = 0
                        bullet_speed = 35
                        pygame.mixer.Sound("assets/sounds/buy_1.mp3").play()
                        score -= 90
                        running = False
                    else:
                        pygame.mixer.Sound("assets/sounds/buzzer.wav").play()
                elif shop9.collidepoint(event.pos):
                    if score >= 110:
                        bullet_amount = 6
                        lastbulletamount = 6
                        shots_fired = 0
                        bullet_speed = 40
                        pygame.mixer.Sound("assets/sounds/buy_1.mp3").play()
                        score -= 110
                        running = False
                    else:
                        pygame.mixer.Sound("assets/sounds/buzzer.wav").play()
                elif shop10.collidepoint(event.pos):
                    if score >= 20 and shield_boom < 3:
                        shield_boom += 1
                        pygame.mixer.Sound("assets/sounds/buy_1.mp3").play()
                        score -= 20
                        running = False
                    else:
                        pygame.mixer.Sound("assets/sounds/buzzer.wav").play()
                elif shop11.collidepoint(event.pos):
                    if score >= 35 and shield_boom < 2:
                        shield_boom += 2
                        pygame.mixer.Sound("assets/sounds/buy_1.mp3").play()
                        score -= 35
                        running = False
                    else:
                        pygame.mixer.Sound("assets/sounds/buzzer.wav").play()
                elif shop12.collidepoint(event.pos):
                    if score >= 50 and shield_boom == 0:
                        shield_boom += 3
                        pygame.mixer.Sound("assets/sounds/buy_1.mp3").play()
                        score -= 50
                        running = False
                    else:
                        pygame.mixer.Sound("assets/sounds/buzzer.wav").play()
                elif shop13.collidepoint(event.pos):
                    if score >= 30 and lives < 5:
                        lives += 1
                        pygame.mixer.Sound("assets/sounds/buy_1.mp3").play()
                        score -= 30
                        running = False
                    else:
                        pygame.mixer.Sound("assets/sounds/buzzer.wav").play()
                elif shop14.collidepoint(event.pos):
                    if score >= 50  and lives < 4:
                        lives += 2
                        pygame.mixer.Sound("assets/sounds/buy_1.mp3").play()
                        score -= 50
                        running = False
                    else:
                        pygame.mixer.Sound("assets/sounds/buzzer.wav").play()
                elif shop15.collidepoint(event.pos):
                    if score >= 100  and lives < 5:
                        lives = 5
                        pygame.mixer.Sound("assets/sounds/buy_1.mp3").play()
                        score -= 100
                        running = False
                    else:
                        pygame.mixer.Sound("assets/sounds/buzzer.wav").play()
                if shop_rect.collidepoint(event.pos):
                    running = False
        draw_shopscreen()
        pygame.display.update()        
    return score, bullet_speed, shield_boom, lives, bullet_amount,shots_fired
