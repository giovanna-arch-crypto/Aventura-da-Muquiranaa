import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
pygame.display.set_caption('Muquirana Life')
player_pos = pygame.Vector2(screen.get_width() / 1.5, screen.get_height() / 1.5)
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
    screen.fill("purple")
    pygame.draw.circle(screen, "red", player_pos, 40)
    key = pygame.key.get_pressed()
    if key[pygame.K_d]:
        player_pos.x += 300 * dt
    if key[pygame.K_a]:
        player_pos.x -= 300 * dt
    pygame.display.update()
    pygame.display.flip()
    dt = clock.tick(60) / 1000
