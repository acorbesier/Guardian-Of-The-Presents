import pygame
import sys
import random
import math
import cv2
from settings import *
from end_screen import *
from pausescreen import *
from santa import *
from shopscreen import *
from start_screen import *
from grinch import RunGrinch 
from settingscreen import *
from weapons import draw_weapon


pygame.init()
pygame.mixer.init()

pygame.mixer.music.set_volume(0.5)
start_geluid.set_volume(0.5)
wave.set_volume(0.5)

            

screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
wave = pygame.mixer.Sound('assets/sounds/wave.mp3')
reload = pygame.mixer.Sound('assets/sounds/gunshots/reload.mp3')
noammo = pygame.mixer.Sound('assets/sounds/gunshots/no-ammo.mp3')
info = pygame.display.Info()
X = info.current_w
Y = info.current_h
last_direction = 1
font = pygame.font.Font("assets/font/PixelatedEleganceRegular-ovyAA.ttf", 42)

firing = False
last_shot_time = 0
fire_rate = 200


coin_image = pygame.image.load("assets/images/coin.png").convert_alpha()
coin_image = pygame.transform.scale(coin_image, (50, 50))  # Resize to 50x50 pixels
gift_image = pygame.image.load("assets/images/gift.png").convert_alpha()
gift_image = pygame.transform.scale(gift_image, (65, 65))  # Resize to 50x50 pixels
shield_image = pygame.image.load("assets/images/shield.png").convert_alpha()
shield_image = pygame.transform.scale(shield_image, (40, 40))  # Resize to 50x50 pixels

icon_image = pygame.image.load("assets/images/logo-500x500.png")  # Path to your icon image
pygame.display.set_icon(icon_image)  # Set the icon

video_capture = cv2.VideoCapture('assets/images/background-animated.mov')

# Sprites groepen
moving_sprites = pygame.sprite.Group() # groep voor santa
enemy_sprites = pygame.sprite.Group()  # Groep voor vijanden

idle_santa = IdleSanta(300, 400, size=(64, 64))
run_santa = RunSanta(300, 400, size=(64, 64))
moving_sprites.add(idle_santa)

rotation_angle = 270
# Functie om vijanden te spawnen

frames = []
for _ in range(5):
    ret, frame = video_capture.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frames.append(frame)

pygame.mixer.music.load('assets/sounds/menu.wav')  
pygame.mixer.music.play(loops=-1)

def spawn_enemy():
    global enemy_count
    side = random.choice(["topleft","topright", "bottom", "left", "right"])
    if side == "topleft":
        enemy_x = random.randint(0, screen_width - 900)
        enemy_y = -64
    elif side == "topright":
        enemy_x = random.randint(screen_width - 400, screen_width - 64)
        enemy_y = -64
    elif side == "bottom":
        enemy_x = random.randint(0, screen_width - 64)
        enemy_y = screen_height
    elif side == "left":
        enemy_x = -64
        enemy_y = random.randint(0, screen_height - 64)
    else:  # right
        enemy_x = screen_width
        enemy_y = random.randint(0, screen_height - 64)
    
    grinch_enemy = RunGrinch(enemy_x,enemy_y, size=(64,64))
    enemy_sprites.add(grinch_enemy)
    enemy_count += 1
    
# Functie om botsingen te controleren
enemy_count = 0
def check_collision():
    global running
    global end_screen
    global lives
    global enemy_count
    global score
    global shield_boom

    
    # for enemy in enemy_sprites:
    #     if isinstance(enemy, RunGrinch):
    #         if abs(enemy.rect.centerx - screen_width // 2) < 5 and abs(enemy.rect.centery - screen_height // 2) < 5 and lives > 0:
    #             lives -= 1
    #             enemy_count -= 1
    #             enemy_sprites.remove(enemy)
    #         if abs(enemy.rect.centerx - screen_width // 2) < 5 and abs(enemy.rect.centery - screen_height // 2) < 5 and lives ==0:
    #             end_screen = True
    
    for enemy in enemy_sprites:
        if isinstance(enemy, RunGrinch):
            if abs(enemy.rect.colliderect(boom1)) and lives > 0 and shield_boom > 0:
                shield_boom -= 1
                enemy_count -= 1
                enemy_sprites.remove(enemy)
            elif abs(enemy.rect.colliderect(boom1)) and lives > 0:
                lives -= 1
                enemy_count -= 1
                enemy_sprites.remove(enemy)
            if abs(enemy.rect.colliderect(boom1)) and lives == 0:
                end_screen = True
def reset():
    global end_screen, running, tijd, wave_tijd, shop, pausescreen_time, wave_count,shots_fired, start_reload_tijd, powerup, score, lives, enemy_count, bullet_speed, bullet_amount, spawn_rate, player_x, player_y, bullets, start_screen_time
    end_screen = False
    running = True
    tijd = pygame.time.get_ticks()
    wave_tijd = 20000
    shop = False
    start_screen_time = 0
    pausescreen_time = 0
    wave_count = 1
    shots_fired = 0
    start_reload_tijd = None
    powerup = False
    score = 0
    lives = 5
    enemy_count = 0
    bullet_speed = 10
    bullet_amount = 12
    spawn_rate = 0.01
    player_x = screen_width / 2 - 25
    player_y = (screen_height / 2) + 200
    enemy_sprites.empty()
    bullets = []

reset()
start = True
while running:
    if start:
        start_screen_time_start = pygame.time.get_ticks()
        start_screen(reload, noammo, wave)
        start_screen_time_end = pygame.time.get_ticks()
        start_screen_time = start_screen_time_end - start_screen_time_start
        start = False
    screen.fill(WHITE)
    ret, frame = video_capture.read()
    ret, frame = video_capture.read()
    if not ret:
        video_capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_resized = cv2.resize(frame, (screen_width, screen_height))
    frame_rotated = pygame.transform.rotate(pygame.surfarray.make_surface(frame_resized), rotation_angle)
    frame_rect = frame_rotated.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(frame_rotated, frame_rect)

    boom1 = pygame.Rect((screen_width / 2.07, screen_height / 2.4, screen_width / 25, height /8))
    #pygame.draw.rect(screen,RED,(screen_width / 2.07, screen_height / 2.4, screen_width / 25, height / 8))
    
    house = pygame.Rect((screen_width / 2.3, screen_height / 100, screen_width / 7.5, height / 8.5))
    #pygame.draw.rect(screen, RED,(screen_width / 2.3, screen_height / 100, screen_width / 7.5, height / 8.5))
    if shop and enemy_count == 0:
        shop_interaction = pygame.Rect((screen_width / 2.3, screen_height / 7, screen_width / 7.5, height / 8))
        #pygame.draw.rect(screen, RED, (screen_width / 2.3, screen_height / 7, screen_width / 7.5, height / 8))
        transparent_surface = pygame.Surface((screen_width / 7.5, height / 12), pygame.SRCALPHA)
        transparent_surface.fill((255, 0, 0, 50))  
        screen.blit(transparent_surface, (screen_width / 2.3, screen_height / 5.1))
    
    collision_objects = [boom1, house]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # geen spray wapens
        if bullet_speed == 10 or bullet_speed == 13 or bullet_speed == 20 or bullet_speed == 35 or bullet_speed == 40:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if shots_fired == bullet_amount:
                    #insert sound lege gun
                    noammo.play()
                    break
                shots_fired += 1
                mouse_x, mouse_y = pygame.mouse.get_pos()
                direction_x = mouse_x - (player_x + player_width // 2)
                direction_y = mouse_y - (player_y + player_height // 2)
                magnitude = math.sqrt(direction_x**2 + direction_y**2)
                if magnitude != 0:
                    direction_x /= magnitude
                    direction_y /= magnitude
                bullets.append([player_x + player_width // 2, player_y + player_height // 2, direction_x, direction_y])
        #spray wapens
        else:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if shots_fired < bullet_amount:
                    firing = True
                else:
                    noammo.play()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                firing = False
    #spray functionaliteit
    if firing:
        current_time = pygame.time.get_ticks()  
        if current_time - last_shot_time > fire_rate:  
            if shots_fired < bullet_amount:
                shots_fired += 1
                mouse_x, mouse_y = pygame.mouse.get_pos()
                direction_x = mouse_x - (player_x + player_width // 2)
                direction_y = mouse_y - (player_y + player_height // 2)
                magnitude = math.sqrt(direction_x**2 + direction_y**2)
                if magnitude != 0:
                    direction_x /= magnitude
                    direction_y /= magnitude
                bullets.append([player_x + player_width // 2, player_y + player_height // 2, direction_x, direction_y])
                last_shot_time = current_time  
            else:
                noammo.play()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        start_reload_tijd = pygame.time.get_ticks()
        # print(pygame.time.get_ticks()- start_reload_tijd)
        reload.play()
    
    if start_reload_tijd is not None and pygame.time.get_ticks() - start_reload_tijd > 2000:
        shots_fired = 0
        start_reload_tijd = None
    
    from settingscreen import keyboard
    if keyboard == "Qwerty":
        if keys[pygame.K_w]:  
            player_velocity_y = -player_speed
        elif keys[pygame.K_s]:  
            player_velocity_y = player_speed
        else:
            player_velocity_y = 0
        if keys[pygame.K_a]:  
            player_velocity_x = -player_speed
            run_santa.direction_x = -1
            last_direction = -1
        elif keys[pygame.K_d]:  
            player_velocity_x = player_speed
            run_santa.direction_x = 1
            last_direction = 1
        else:
            player_velocity_x = 0
    else:
        player_velocity_x = 0
        if keys[pygame.K_z]:  
            player_velocity_y = -player_speed
        elif keys[pygame.K_s]:  
            player_velocity_y = player_speed
        else:
            player_velocity_y = 0

        if keys[pygame.K_q]:  
            player_velocity_x = -player_speed
            run_santa.direction_x = -1
            last_direction = -1
        elif keys[pygame.K_d]:  
            player_velocity_x = player_speed
            run_santa.direction_x = 1
            last_direction = 1
        else:
            player_velocity_x = 0
    
    # Update player position
    player_x += player_velocity_x
    player_y += player_velocity_y

    # Define player's rectangle
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

    # Check collisions with static objects
    for obj in collision_objects:
        if player_rect.colliderect(obj):
            # Revert the player's movement
            player_x -= player_velocity_x
            player_y -= player_velocity_y
            break

    # Ensure the player stays within the screen bounds
    player_x = max(0, min(player_x, screen_width - player_width))
    player_y = max(0, min(player_y, screen_height - player_height))

    if powerup:
        powerup_image = pygame.image.load("assets/abilities/dubble-coin.png").convert_alpha()
        powerup_image = pygame.transform.scale(powerup_image, (100, 100))  # Resize to 50x50 pixels
        screen.blit(powerup_image, (screen_width-X/(11), screen_height-Y/(6)))


    # Update kogels
    for bullet in bullets[:]:
        bullet[0] += bullet_speed * bullet[2]
        bullet[1] += bullet_speed * bullet[3]
        if bullet[0] < 0 or bullet[1] < 0 or bullet[0] > screen_width or bullet[1] > screen_height:
            bullets.remove(bullet)

    # Update vijanden
    enemy_sprites.update()  # Laat de Grinch bewegen

    check_collision()

    for bullet in bullets[:]:
        for enemy in enemy_sprites:
            if enemy.rect.collidepoint(bullet[0], bullet[1]):
                bullets.remove(bullet)
                enemy_count -= 1
                # print(enemy_count)
                enemy_sprites.remove(enemy)
                if powerup:
                    score += 4
                else:
                    score += 2
                if random.random() < 0.02:
                    powerup = True
                break

    # Update speleranimatie
    if player_velocity_x != 0 or player_velocity_y != 0:  # Beweegt
        run_santa.rect.topleft = (player_x, player_y)
        moving_sprites.empty()
        moving_sprites.add(run_santa)
    else:  # Staat stil
        idle_santa.rect.topleft = (player_x, player_y)
        moving_sprites.empty()
        moving_sprites.add(idle_santa)
        idle_santa.direction_x = last_direction

    moving_sprites.draw(screen)
    moving_sprites.update()
    enemy_sprites.draw(screen)  # Teken de vijanden

    # Teken kogels
    for bullet in bullets:
        pygame.draw.rect(screen, BLACK, (bullet[0], bullet[1], bullet_width, bullet_height))

    # Blit images and render text, aligned vertically under each other
    screen.blit(coin_image, (5, 0))  # Coin image
    score_text = font.render(f"{score}", True, BLACK)
    screen.blit(score_text, (60, 10))  # Score text next to the coin image

    screen.blit(gift_image, (-4, 40))  # Lives (gift) image
    gift_text = font.render(f"{lives}/5", True, BLACK)
    screen.blit(gift_text, (60, 60))  # Lives text next to the gift image

    screen.blit(shield_image, (10, 105))  # Shield image
    shield_text = font.render(f"{shield_boom}", True, BLACK)
    screen.blit(shield_text, (60, 105))  # Shield text next to the shield image
    
    ammo_screen = font.render(f"{bullet_amount-shots_fired}/{bullet_amount}", True, BLACK)
    screen.blit(ammo_screen, (screen_width-X/(10), 10))

    # Render and display wave text
    if shop and enemy_count == 0:
        wave_text = font.render(f"Press space for wave: {wave_count + 1}", True, BLACK)
    else:
        wave_text = font.render(f"Wave: {wave_count}", True, BLACK)
    screen.blit(wave_text, (10, 155))  # Wave text aligned under shield

    if shop and enemy_count == 0 and keys[pygame.K_e] and shop_interaction.collidepoint(player_x + player_width, player_y + player_height):
        output = shopscreen(score, bullet_speed, shield_boom, lives, bullet_amount,shots_fired)
        score = output[0]
        bullet_speed = output[1]
        shield_boom = output[2]
        lives = output[3]
        bullet_amount = output[4]
        shots_fired = output[5]

    draw_weapon(bullet_speed, player_x, player_y, player_velocity_x, last_direction)
    pygame.display.flip()
    
    # print(pygame.time.get_ticks() - tijd - start_screen_time - pausescreen_time)
    if pygame.time.get_ticks() - tijd - start_screen_time - pausescreen_time < wave_tijd:
        shop = False
        if random.random() < spawn_rate:
            spawn_enemy()
    else:
        if enemy_count == 0:
            powerup = False
        shop = True

    if end_screen:
        start_screen_time = main(wave, reload, noammo)
        reset()
        end_screen = False
        
    #esc opent pause menu
    if keys[pygame.K_ESCAPE]:
        pausescreen_time_start = pygame.time.get_ticks()
        reset_ = pausescreen(wave, reload, noammo)
        pausescreen_time_end = pygame.time.get_ticks()
        pausescreen_time += pausescreen_time_end - pausescreen_time_start
        if reset_:
            reset()

    # print(shop)
    # print(enemy_count)  
    if keys[pygame.K_SPACE] and enemy_count == 0 and shop:
        pausescreen_time = 0
        tijd = pygame.time.get_ticks()
        spawn_rate += 0.006
        start_screen_time = 0
        wave_count += 1
        shop = False
        wave.play()


    clock.tick(30)

video_capture.release()
pygame.quit()
sys.exit()