import pygame
import random
import Enemy
import Player


pygame.init()



width = 1000
height = 1000
white = (255, 255, 255)



width = 1000
height = 1000
green = (0, 255, 0)

win = pygame.display.set_mode((width, height))


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
    pygame.draw.rect(win, green, (200, 680, 100, 100))
    pygame.draw.rect(win, green, (300, 680, 100, 100))
    pygame.display.update()




    all_sprites.draw(win)
    enemy_sprites.draw(win)
    player.jump()

    # Обновляем спрайты
    all_sprites.update()
    enemy_sprites.update()
    pygame.display.update()
    clock.tick(FPS)

