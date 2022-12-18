import pygame

width = 1000
height = 1000

win = pygame.display.set_mode((width, height))

class Player(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()

        self.image = pygame.image.load('3F3F3F3F_3F3F.webp')

        self.image = self.image.convert()
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.top = height - 200

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.rect.left > 0:
                self.rect.left -= 5
        if keys[pygame.K_RIGHT]:
            if self.rect.right < width:
                self.rect.left += 5
