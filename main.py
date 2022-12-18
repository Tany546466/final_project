import pygame
import random
import Player

pygame.init()

width = 1000
height = 1000


win = pygame.display.set_mode((width, height))

white = (255, 255, 255)

FPS = 60
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player.Player()
all_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill(white)
    # Рисуем все спрайты, который есть в группе
    all_sprites.draw(win)

    # Обновляем спрайты
    all_sprites.update()

    pygame.display.update()
    clock.tick(FPS)

