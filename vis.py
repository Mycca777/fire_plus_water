# огонь и вода
import pygame
from PIL import Image
from light import *
from flame import *
from character import *
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
character = Character('character.png')
button_pos = (300, 591)
platform_pos_standart = platform_pos = (35, 300)
counter = 0


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
            if e.key == pygame.K_RIGHT:
                motion = 'RIGHT'
            if e.key == pygame.K_UP:
                motion = 'UP'
            # elif e.key == pygame.K_DOWN:
            #     motion = 'DOWN'
        elif e.type == pygame.KEYUP:
            motion = None
    # screen.blit(mask.image, character)
    for i in range(len(all_pos)):
        put_light_source(surf, mask, all_pos[i], EMBIANT_COLOR[random.randint(1, 15)])
        flame[i].draw_flame()

    platform = Platform(platform_pos, mask, screen, platform_pos_standart, counter)
    character.move(motion)
    color = character.collision(mask, platform)
    character.isjump = False
    character.draw(surf, screen, color)
    button = Button(button_pos, mask, screen)
    button.is_button_pressed(character)
    counter, platform_pos = platform.platform_move(button, character)
    if button.is_button_pressed(character):
        put_light_source(surf, mask, (platform_pos[0] + 40, platform_pos[1]+10), (0,100,0))
    # pygame.draw.circle(screen, (255,255,255), (platform_pos[0] + 40, platform_pos[1]+10), 1)
    pygame.display.update()
