import pygame
import random
import Enemy
import Player

pygame.init()

width = 1000
height = 1000
white = (255, 255, 255)

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

win = pygame.display.set_mode((width, height))


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

block3 = Blocks()
block3.rect.left = 400
block_sprites.add(block3)

background_image = pygame.image.load('background.png')
background_image1 = pygame.image.load('background.png')
background_1X = 0
background_2X = background_image.get_width()

# Противник нас "ударил"
kick = False

background_speed = 3

terrain = pygame.image.load('terrain.jpg')
terrain = pygame.transform.scale(terrain, (100, 100))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()

    win.blit(background_image, (background_1X, 0))
    win.blit(background_image1, (background_2X, 0))

    f1 = pygame.font.Font(None, 36)
    text1 = f1.render(str(player.health), 1, (180, 0, 0))
    win.blit(text1, (10, 50))
    for i in range(0, 10, 1):
        win.blit(terrain, (i * 100, 900))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        background_1X -= background_speed
        background_2X -= background_speed
        for block in block_sprites:
            block.rect.left -= background_speed

    if background_1X + background_image.get_width() <= 0:
        background_1X = background_image.get_width()
    if background_2X + background_image1.get_width() <= 0:
        background_2X = background_image1.get_width()

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
        if hit == False:
            player.health -= 1
            hit = True
    else:
        hit = False
    enemy_sprites.update()
    block_sprites.update()
    pygame.display.update()
    clock.tick(FPS)
