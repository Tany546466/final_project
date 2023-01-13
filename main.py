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
        self.rect.top = 650


pygame.init()
height = 1000
width = 1000
green = (0, 255, 0)
win = pygame.display.set_mode((width, height))

white = (0, 155, 170)

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

block2 = Blocks()
block2.rect.left = 300
block_sprites.add(block2)


background_image = pygame.image.load('background.png')
background_image1 = pygame.image.load('background.png')
background_x = 0
background_x1 = background_image.get_width()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()




    win.fill(white)
    win.blit(background_image, (background_x, 0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        background_x -= 5
        background_x1 -= 5
    if background_x + background_image.get_width() <= 0:
        background_x = background_image.get_width()
    if background_x1 + background_image1.get_width() <= 0:
        background_x1 = background_image1.get_width()

    pygame.draw.rect(win, green, (100, 650, 100, 100))
    pygame.draw.rect(win, green, (200, 650, 100, 100))
    pygame.draw.rect(win, green, (500, 650, 100, 100))
    pygame.draw.rect(win, green, (600, 650, 100, 100))
    all_sprites.draw(win)
    enemy_sprites.draw(win)
    block_sprites.draw(win)
    player.jump()
    all_sprites.update()
    hits_block = pygame.sprite.spritecollide(player, block_sprites, True)
    hits_enemy = pygame.sprite.spritecollide(player, enemy_sprites, False)
    if player.rect.bottom >= enemy.rect.top - 10 and player.rect.bottom <= enemy.rect.top + 10 and player.rect.right >= enemy.rect.left and player.rect.left <= enemy.rect.right:
        enemy_sprites.remove(enemy)
    if len(hits_enemy) != 0:
        player.health -= 1
    enemy_sprites.update()
    block_sprites.update()
    pygame.display.update()
    clock.tick(FPS)

