import pygame

pygame.init()

width = 500
height = 500

win = pygame.display.set_mode((width, height))

white = (255, 255, 255)

FPS = 60
clock = pygame.time.Clock()

def load_img(name):
    img = pygame.image.load(name)
    img = img.convert()
    colorkey = img.get_at((0, 0))
    img.set_colorkey(colorkey)
    return img

class Inginirium(pygame.sprite.Sprite):

    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_img('')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width)
        self.rect.y = random.randrange(height)



class PlayerObject:
    def __init__(self):
        self.health = 5
        self.width = 0
        self.height = 0
        self.image = pygame.image.load('*путь до файла*')
        self.rect = self.image.get_rect()
    def move_up(self):
        pass
    def move_down(self):
        pass
    def move_left(self):
        pass
    def move_right(self):
        pass

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill(white)
    pygame.display.update()
    clock.tick(FPS)

