'''
character
'''
import pygame


class Character:
    def __init__(self):
        self.character_pos = [100, 500]
        self.character_image = pygame.image.load('character.png')
        self.hitbox_size = 50
        self.is_touching = [False, False, False, False]

    def move(self, motion):
        if motion == 'LEFT':
            self.character_pos[0] -= 5
        elif motion == 'RIGHT':
            self.character_pos[0] += 5
        elif motion == 'UP':
            self.character_pos[1] -= 5
        elif motion == 'DOWN':
            self.character_pos[1] += 5

    def draw(self, surf, screen, color=(255,0,0,200)):
        pygame.draw.rect(surf, color, (self.character_pos[0]-self.hitbox_size/2, self.character_pos[1]-self.hitbox_size/2, self.hitbox_size, self.hitbox_size),8)
        screen.blit(surf, (0,0))

    def collision(self, mask):
        touching = False
        self.phisical_hitbox_points = [[self.character_pos[0] - self.hitbox_size/2, self.character_pos[1] - self.hitbox_size/2],
                                       [self.character_pos[0] - self.hitbox_size/2, self.character_pos[1]],
                                       [self.character_pos[0] - self.hitbox_size/2, self.character_pos[1] + self.hitbox_size/2],
                                       [self.character_pos[0], self.character_pos[1] - self.hitbox_size/2],
                                       [self.character_pos[0], self.character_pos[1] + self.hitbox_size/2],
                                       [self.character_pos[0] + self.hitbox_size/2, self.character_pos[1] - self.hitbox_size/2],
                                       [self.character_pos[0] + self.hitbox_size/2, self.character_pos[1]],
                                       [self.character_pos[0] + self.hitbox_size/2, self.character_pos[1] + self.hitbox_size/2]]
        # pos_in_mask = self.character_pos[0] - mask.rect.x, self.character_pos[1] - mask.rect.y    
        for cords in self.phisical_hitbox_points:
            pos_in_mask = cords[0] - mask.rect.x, cords[1] - mask.rect.y
            print(pos_in_mask)
            print(mask.mask.get_at(pos_in_mask))
            touching = mask.rect.collidepoint(*cords) and mask.mask.get_at(pos_in_mask)
            print(touching)
            if touching == True:
                break
        if touching:

            color = (255, 255, 255)
        else:
            color = (255,0,0,200)
        return color
