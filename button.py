'''
Button
'''
import pygame


BUTTON_FILES = ['button_casual.png', 'button_pressed.png']

class Button:
    def __init__(self, button_pos, mask, surface):
        self.surface = surface
        self.button_pos = button_pos[0] - mask.rect.x, button_pos[1] - mask.rect.y
        self.images = []
        self.images.append(pygame.image.load('button_casual.png').convert_alpha())
        self.images.append(pygame.image.load('button_pressed.png').convert_alpha())
        for i in range(len(self.images)):
            self.images[i] = pygame.transform.scale(self.images[i], (40,10))
        self.button_hitbox = pygame.Rect(self.button_pos[0] + 15, self.button_pos[1] + 13, 30, 10)

    def is_button_pressed(self, character, character1):
        '''
        character has: rect(hitbox), pos(of centre hitbox)
        '''
        character_hitbox = character.hitbox
        character1_hitbox = character1.hitbox
        touching = pygame.Rect.colliderect(character_hitbox, self.button_hitbox)
        touching1 = pygame.Rect.colliderect(character1_hitbox, self.button_hitbox)
        # print(touching)
        if touching or touching1:
            self.draw(self.images[1], (self.button_pos[0]-15, self.button_pos[1]-15))
            return True
        else:
            self.draw(self.images[0], (self.button_pos[0]-15, self.button_pos[1]-15))
            return False

    def draw(self, image, pos):
        self.surface.blit(image, pos)


class Platform:
    def __init__(self, platform_pos, mask, surface, platform_pos_standart, counter):
        self.surface = surface
        self.platform_pos_standart = list((platform_pos_standart[0] - mask.rect.x, platform_pos_standart[1] - mask.rect.y))
        self.platform_pos = self.platform_pos_standart
        self.counter = counter
        self.images = []
        self.images.append(pygame.image.load('platform_casual.png').convert_alpha())
        self.images.append(pygame.image.load('platform_bright.png').convert_alpha())
        self.platform_hitbox = pygame.Rect(self.platform_pos[0] + 43, self.platform_pos[1] + 23, 40, 10)
        self.distance_to_move = 60

    def platform_move(self, button, character, character1):
        clock = pygame.time.Clock()
        if button.is_button_pressed(character, character1):
            if self.counter < self.distance_to_move/5:
                self.platform_pos[1] += 5*self.counter
                self.counter += 1
            else:
                self.platform_pos[1] = self.platform_pos_standart[1] + self.distance_to_move
            self.image = self.images[1]
            self.draw(self.images[1], self.platform_pos)
        else:
            if self.counter != 0:
                self.platform_pos[1] += 5*self.counter
                self.counter -= 1
            self.image = self.images[0]
            self.draw(self.images[0], self.platform_pos)
        return self.counter, self.platform_pos

    def collision(self, character_hitbox):
        touching = pygame.Rect.colliderect(character_hitbox, self.platform_hitbox)
        if touching:
            return True
        else:
            return False

    def draw(self, image, pos):
        self.surface.blit(image, pos)

