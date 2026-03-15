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
                    timer = pygame.time.get_ticks()
                    if position:
                        timer -= position
                else:
                    pygame.mixer.music.pause()
                    PLAY_BUTTON.update_icon(PLAY_ICON_PATH)
                    position = pygame.time.get_ticks()
                    if timer:
                        position -= timer
    if timer:
        elapsed_time = (pygame.time.get_ticks() - timer)
        if elapsed_time >= MAX_TIME:
            pygame.mixer.music.stop()
            PLAY_BUTTON.update_icon(PLAY_ICON_PATH)
            timer = 0
            position = 0
        
    screen.fill((30, 30, 30))

    PLAY_BUTTON.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
