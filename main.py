import pygame
import random

import Enemy
import Player


class Blocks(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('1623135234_7-phonoteka_org-p-pikselnaya-tekstura-kamnya-krasivo-8.png')
        self.image = self.image.convert()
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.top = 700

pygame.init()
height = 1000
width = 1000
green = (0, 255, 0)

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


block = Blocks()
block_sprites = pygame.sprite.Group()
block_sprites.add(block)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()




    win.fill(white)
    pygame.draw.rect(win, green, (100, 700, 100, 100))
    pygame.draw.rect(win, green, (200, 700, 100, 100))
    pygame.draw.rect(win, green, (500, 700, 100, 100))
    pygame.draw.rect(win, green, (600, 700, 100, 100))
    all_sprites.draw(win)
    enemy_sprites.draw(win)
    block_sprites.draw(win)
    player.jump()
    all_sprites.update()
    hits = pygame.sprite.spritecollide(player, block_sprites, False)

    enemy_sprites.update()
    block_sprites.update()
    pygame.display.update()
    clock.tick(FPS)

