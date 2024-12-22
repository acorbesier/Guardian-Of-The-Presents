import pygame
import sys


pygame.init()


info = pygame.display.Info()
width = info.current_w
height = info.current_h

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Settings")
clock = pygame.time.Clock()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

font = pygame.font.Font(None, 74)
button_font = pygame.font.Font(None, 50)

settings_text = font.render("Settings", True, RED)


menu_button = pygame.Rect(width // 2 - 100, height // 2 + 70, 200, 50)
quit_button = pygame.Rect(width // 2 - 100, height // 2 + 140, 200, 50)



slider_x = width // 2 - 150
slider_y = height // 2 + 25
slider_width = 300
slider_height = 10
slider_rect = pygame.Rect(slider_x, slider_y, slider_width, slider_height)

handle_radius = 15
handle_x = slider_x + slider_width // 2  
volume = 0.5  

def draw_settings_screen():
    """Tekent het instellingenmenu."""
    screen.fill(BLACK)
    screen.blit(settings_text, (width // 2 - settings_text.get_width() // 2, height // 3))
    
    # Volume slider
    pygame.draw.rect(screen, GRAY, slider_rect)  
    pygame.draw.circle(screen, GREEN, (handle_x, slider_y + slider_height // 2), handle_radius)  # Handle
    volume_text = button_font.render(f"Volume: {int(volume * 100)}%", True, WHITE)
    screen.blit(volume_text, (slider_x, slider_y - 40))  # Display volume value

    # Menu button
    pygame.draw.rect(screen, GRAY, menu_button)
    menu_text = button_font.render(keyboard, True, WHITE)
    screen.blit(menu_text, (menu_button.x + (menu_button.width - menu_text.get_width()) // 2,
                            menu_button.y + (menu_button.height - menu_text.get_height()) // 2))
    
    # Quit button
    pygame.draw.rect(screen, GRAY, quit_button)
    quit_text = button_font.render("Back", True, WHITE)
    screen.blit(quit_text, (quit_button.x + (quit_button.width - quit_text.get_width()) // 2,
                            quit_button.y + (quit_button.height - quit_text.get_height()) // 2))

keyboard = "Azerty"

def settingscreen(wave, reload, noammo):
    global keyboard, handle_x, volume
    running = True
    dragging = False  
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            from start_screen import start_geluid

            pygame.mixer.music.set_volume(volume)
            start_geluid.set_volume(volume)
            wave.set_volume(volume)
            reload.set_volume(volume)
            noammo.set_volume(volume)


            if event.type == pygame.MOUSEBUTTONDOWN:
                
                mouse_x, mouse_y = event.pos
                if (handle_x - handle_radius <= mouse_x <= handle_x + handle_radius and
                        slider_y - handle_radius <= mouse_y <= slider_y + handle_radius):
                    dragging = True

                
                if menu_button.collidepoint(event.pos):
                    if keyboard == "Azerty":
                        keyboard = "Qwerty"
                    else:
                        keyboard = "Azerty"
                if quit_button.collidepoint(event.pos):
                    running = False

            if event.type == pygame.MOUSEBUTTONUP:
                dragging = False  

            if event.type == pygame.MOUSEMOTION and dragging:
                
                mouse_x, _ = event.pos
                handle_x = max(slider_x, min(mouse_x, slider_x + slider_width))  
                volume = (handle_x - slider_x) / slider_width  

       
        draw_settings_screen()
        pygame.display.flip()
        clock.tick(60)


