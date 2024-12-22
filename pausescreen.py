import pygame
import sys
from settingscreen import *
from start_screen import start_screen

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


font = pygame.font.Font(None, 74)
button_font = pygame.font.Font(None, 50)


settings_title_text = font.render("Paused", True, RED)


button_width, button_height = 200, 50
button_spacing = 20  


menu_button = pygame.Rect(width // 2 - button_width // 2, height // 2, button_width, button_height)
settings_button = pygame.Rect(
    width // 2 - button_width // 2,
    menu_button.bottom + button_spacing,
    button_width,
    button_height
)
menu_button_button = pygame.Rect(
    width // 2 - button_width // 2,
    settings_button.bottom + button_spacing,
    button_width,
    button_height
)

def draw_settings_screen():
    """Tekent het instellingenmenu."""
    screen.fill(BLACK)
    
    # Title text
    screen.blit(settings_title_text, (width // 2 - settings_title_text.get_width() // 2, height // 4))
    
    # Menu button
    pygame.draw.rect(screen, GRAY, menu_button)
    menu_text = button_font.render("Resume", True, WHITE)
    screen.blit(menu_text, (menu_button.x + (menu_button.width - menu_text.get_width()) // 2,
                            menu_button.y + (menu_button.height - menu_text.get_height()) // 2))
    
    # Settings button
    pygame.draw.rect(screen, GRAY, settings_button)
    settings_button_text = button_font.render("Settings", True, WHITE)  # Renamed local variable
    screen.blit(settings_button_text, (settings_button.x + (settings_button.width - settings_button_text.get_width()) // 2,
                                       settings_button.y + (settings_button.height - settings_button_text.get_height()) // 2))
    
    # Quit button
    pygame.draw.rect(screen, GRAY, menu_button_button)
    quit_text = button_font.render("Menu", True, WHITE)
    screen.blit(quit_text, (menu_button_button.x + (menu_button_button.width - quit_text.get_width()) // 2,
                            menu_button_button.y + (menu_button_button.height - quit_text.get_height()) // 2))

def pausescreen(wave, reload, noammo):
    running = True
    while running:
        draw_settings_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_button.collidepoint(event.pos):
                    running = False
                    reset = False
                    print("Resume clicked!")
                if settings_button.collidepoint(event.pos):
                    settingscreen(wave, reload, noammo)
                    reset = False
                    print("Settings clicked!")
                if menu_button_button.collidepoint(event.pos):
                    print("Quit clicked!")
                    reset = True
                    running = False
                    start_screen(wave, reload, noammo)

                
        
    
                
        pygame.display.flip()
        clock.tick(60)
    return reset
