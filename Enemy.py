import pygame

width = 1000
height = 1000

win = pygame.display.set_mode((width, height))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Greennew.webp')
        self.image = self.image.convert_alpha()
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.top = height - 200
        self.rect.left = width - self.rect.width
        self.speed = 5

    def update(self):
        self.rect.left -= self.speed
        if self.rect.left == 0 or self.rect.right == width:
            self.speed = -self.speed

