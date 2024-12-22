import pygame
import sys
from start_screen import start_screen

pygame.init()


info = pygame.display.Info()
width = info.current_w
height = info.current_h

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game Over Scherm")
clock = pygame.time.Clock()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (255, 0, 0)


font = pygame.font.Font(None, 74)
button_font = pygame.font.Font(None, 50)


game_over_text = font.render("Game Over", True, RED)


replay_button = pygame.Rect(width // 2 - 100, height // 2, 200, 50)
menu_button = pygame.Rect(width // 2 - 100, height // 2 + 70, 200, 50)
quit_button = pygame.Rect(width // 2 - 100, height // 2 + 140, 200, 50)

def draw_end_screen():
    screen.fill(BLACK)
    screen.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 3))
    
    # Replay button
    pygame.draw.rect(screen, GRAY, replay_button)
    replay_text = button_font.render("Replay", True, WHITE)
    screen.blit(replay_text, (replay_button.x + (replay_button.width - replay_text.get_width()) // 2,
                              replay_button.y + (replay_button.height - replay_text.get_height()) // 2))
    
    # Menu button
    pygame.draw.rect(screen, GRAY, menu_button)
    menu_text = button_font.render("Menu", True, WHITE)
    screen.blit(menu_text, (menu_button.x + (menu_button.width - menu_text.get_width()) // 2,
                            menu_button.y + (menu_button.height - menu_text.get_height()) // 2))
    
    # Quit button
    pygame.draw.rect(screen, GRAY, quit_button)
    quit_text = button_font.render("Quit", True, WHITE)
    screen.blit(quit_text, (quit_button.x + (quit_button.width - quit_text.get_width()) // 2,
                            quit_button.y + (quit_button.height - quit_text.get_height()) // 2))

def main(wave, reload, noammo):
    global startscreen
    running = True
    while running:
        draw_end_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if replay_button.collidepoint(event.pos):
                    print("Replay clicked!")
                    running = False
                    # Voeg logica toe om het spel opnieuw te starten.
                if menu_button.collidepoint(event.pos):
                    running = False
                    start_screen(wave, reload, noammo)
                    print("Menu clicked!")
                    # Voeg logica toe om naar het hoofdmenu te gaan.
                if quit_button.collidepoint(event.pos):
                    print("Quit clicked!")
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(60)

