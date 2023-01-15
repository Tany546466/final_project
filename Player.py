import pygame

width = 1000
height = 1000

win = pygame.display.set_mode((width, height))

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):

        super().__init__()

        self.image = pygame.image.load('3F3F3F3F_3F3F.webp')

        self.image = self.image.convert()
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.top = height - 200
        self.is_jumping = False
        self.jump_count = 10
        self.health = 5

    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.is_jumping = True
        if self.is_jumping:
            if self.jump_count >= -10:
                self.rect.top -= (self.jump_count * abs(self.jump_count) * 0.5)
                self.jump_count -= 1
            else:
                self.jump_count = 10
                self.is_jumping = False

    def update(self):
        '''keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.rect.left > 0:
                self.rect.left -= 5
        if keys[pygame.K_RIGHT]:
            if self.rect.right < width:

                self.rect.left += 5

        pygame.display.update()

        self.rect.left += 5'''

