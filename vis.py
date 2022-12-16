# огонь и вода
import pygame
from light import *
from flame import *
from Character import *
from button import *


EMBIANT_COLOR = [(213, 169 + i, 21, 230) for i in range(25)]
pygame.init()

WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Mask:
    def __init__(self, filename, scale):
        self.image = pygame.image.load(filename).convert_alpha()
        self.image.set_colorkey((0,0,0))
        self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self.mask = pygame.mask.from_surface(self.image)



def put_light_source(surf, mask, pos, color):
    surf.fill((0,0,0,255))
    surf.set_alpha(120)
    cast_all_lights(surf, pos, mask, color)
    surf.blit(light_surf, (pos[0]-WIDTH / 2, pos[1]-HEIGHT / 2))
    screen.blit(surf, (0,0))



light_surf = pygame.image.load('light_mask.png').convert_alpha()
light_surf = pygame.transform.scale(light_surf, (WIDTH, HEIGHT))

screen.fill((0,0,0))
running = True
mask = Mask('map.png', (WIDTH, HEIGHT))
all_pos = [(100, 100), (500, 275), (600, 400)]
flame = [Flame(pos[0], pos[1]) for pos in all_pos]
motion = None
motion1 = None
character = Character('character.png')
character1 = Character('ogon.png')
button_pos = (300, 592)
platform_pos_standart = platform_pos = (35, 300)
counter = 0
is_there_flames = 1
clock = pygame.time.Clock()
FPS = 10


while running:
    screen.fill((0,0,0))
    surf = pygame.Surface((WIDTH, HEIGHT))
    surf.set_colorkey((0,0,0))
    screen.blit(mask.image, mask.rect)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                motion = 'LEFT'
            if e.key == pygame.K_a:
                motion1 = 'LEFT'
            if e.key == pygame.K_RIGHT:
                motion = 'RIGHT'
            if e.key == pygame.K_d:
                motion1 = 'RIGHT'
            if e.key == pygame.K_UP:
                motion = 'UP'
            if e.key == pygame.K_w:
                motion1 = 'UP'
            if e.key == pygame.K_f:
                is_there_flames *= -1
        elif e.type == pygame.KEYUP:
            motion = None
            motion1 = None
    # screen.blit(mask.image, character)
    if is_there_flames > 0:
        for i in range(len(all_pos)):
            put_light_source(surf, mask, all_pos[i], EMBIANT_COLOR[random.randint(1, 15)])
            flame[i].draw_flame()
    else:
        clock.tick(FPS)
    platform = Platform(platform_pos, mask, screen, platform_pos_standart, counter)
    character.move(motion)
    character1.move(motion1)
    color = character.collision(mask, platform)
    color1 = character1.collision(mask, platform)
    character.isjump = False
    character1.isjump = False
    character.draw(surf, screen, color)
    character1.draw(surf, screen, color1)
    button = Button(button_pos, mask, screen)
    button.is_button_pressed(character, character1)
    counter, platform_pos = platform.platform_move(button, character, character1)
    if button.is_button_pressed(character, character1):
        put_light_source(surf, mask, (platform_pos[0] + 40, platform_pos[1]+10), (0,100,0))

    # pygame.draw.circle(screen, (255,255,255), (platform_pos[0] + 40, platform_pos[1]+10), 1)
    pygame.display.update()
