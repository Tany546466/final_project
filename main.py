import pygame
import random

import Enemy
import Player

pygame.init()

width = 1000
height = 1000


win = pygame.display.set_mode((width, height))

white = (255, 255, 255)

FPS = 60
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player.Player(10, 10)
all_sprites.add(player)

enemy_sprites = pygame.sprite.Group()
enemy = Enemy.Enemy()
enemy_sprites.add(enemy)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill(white)
    # Рисуем все спрайты, который есть в группе
    all_sprites.draw(win)
    enemy_sprites.draw(win)
    player.jump()

    # Обновляем спрайты
    all_sprites.update()
    enemy_sprites.update()
    pygame.display.update()
    clock.tick(FPS)

