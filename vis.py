import pygame
from light import *
from flame import *

EMBIANT_COLOR = [(213, 169 + i, 21, 230) for i in range(25)]

pygame.init()

WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Mask:
	def __init__(self, filename, scale):
		self.image = pygame.image.load(filename).convert_alpha()
		self.image.set_colorkey((0, 0, 0))
		self.image = pygame.transform.scale(self.image, scale)
		self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2))
		self.mask = pygame.mask.from_surface(self.image)


def put_light_source(surf, mask, pos, color):
	surf.fill((0, 0, 0, 255))
	surf.set_alpha(120)
	# screen.fill(pygame.Color('red') if touching else pygame.Color('green'))

	cast_all_lights(surf, pos, mask, color)
	surf.blit(light_surf, (pos[0] - WIDTH / 2, pos[1] - HEIGHT / 2))
	screen.blit(surf, (0, 0))


light_surf = pygame.image.load('light_mask.png').convert_alpha()
light_surf = pygame.transform.scale(light_surf, (WIDTH, HEIGHT))

screen.fill((0, 0, 0))
running = True
mask = Mask('map.png', (WIDTH, HEIGHT))
surf = pygame.Surface((WIDTH, HEIGHT))
surf.set_colorkey((0, 0, 0))
all_pos = [(200, 100), (100, 100), (200, 275), (350, 375)]
flame = [Flame(pos[0], pos[1]) for pos in all_pos]

while running:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			running = False
	screen.blit(mask.image, mask.rect)
	for i in range(len(all_pos)):
		put_light_source(surf, mask, all_pos[i], EMBIANT_COLOR[random.randint(1, 15)])
		flame[i].draw_flame()
	# if i < 25:
	#     i += 1
	# else:
	#     i = 0

	pygame.display.update()
