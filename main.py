import pygame
import sys
import button
from settings import *
pygame.init()
pygame.mixer.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Pygame Project")

clock = pygame.time.Clock()

running = True
timer = 0
position = 0
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if PLAY_BUTTON.is_clicked(event.pos):
                if not PLAY_BUTTON.initial:
                    pygame.mixer.music.load('assets/audio/Audio-Demo1.mp3')
                    pygame.mixer.music.play(-1, 80 + (position / 1000))
                    PLAY_BUTTON.update_icon(PAUSE_ICON_PATH)
                    timer = pygame.time.get_ticks() - position
                else:
                    pygame.mixer.music.pause()
                    PLAY_BUTTON.update_icon(PLAY_ICON_PATH)
                    position = pygame.time.get_ticks() - timer
    
    if PLAY_BUTTON.initial:
        position = (pygame.time.get_ticks() - timer) if timer else 0
        if position >= MAX_TIME:
            pygame.mixer.music.stop()
            PLAY_BUTTON.update_icon(PLAY_ICON_PATH)
            timer = 0
            position = 0
        
    screen.fill((30, 30, 30))

    PLAY_BUTTON.draw(screen)

    progress = min(position / MAX_TIME, 1)
    pygame.draw.rect(screen, FONT_COLOR, 
                    (WIDTH // 4, (HEIGHT // 4) - (PLAY_BUTTON.radius // 1.5),
                    WIDTH // 3, int(1.5 * PLAY_BUTTON.radius)),
                    border_radius=15)
    pygame.draw.rect(screen, HIGHLIGHT_COLOR,
                    (WIDTH // 4, (HEIGHT // 4) - (PLAY_BUTTON.radius // 1.5), 
                    int((WIDTH / 3) * progress), int(1.5 * PLAY_BUTTON.radius)),
                    border_radius=15)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
