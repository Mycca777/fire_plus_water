'''
character
'''
import pygame


class Character1:
    def __init__(self, character_image=None):
        self.character_pos1 = [10, 10]
        self.character_image1 = pygame.image.load(character_image).convert_alpha()
        scale = (60, 70)
        self.character_image1 = pygame.transform.scale(self.character_image, scale)
        self.hitbox_size1 = 50
        self.is_touching1 = [False, False, False, False]
        self.vx1 = 0
        self.vy1 = 0

    def move(self, motion1):
        jumpcount = 0
        # по горизонтали
        if motion1 == 'LEFT' and not self.is_touching1[0]:
            self.vx1 = -5
        elif motion1 == 'RIGHT' and not self.is_touching1[1]:
            self.vx1 = 5
        elif self.is_touching1[0] or self.is_touching1[1]:
            self.vx1 = 0
        elif not motion1:
            self.vx1 = 0
        self.character_pos1[0] += self.vx1

        if motion1 == 'UP' and self.is_touching1[3]:
            self.vy1 = 6
            self.is_touching1[3] = False
        elif not self.is_touching1[3]:
            jumpcount += 1
            self.vy1 -= jumpcount / 3
        elif self.is_touching1[3]:
            self.vy1 = 0

        if self.is_touching1[2]:
            self.vy1 = -2

        self.character_pos1[1] -= self.vy1
        self.hitbox1 = pygame.Rect(self.character_pos1[0], self.character_pos1[1], self.hitbox_size1, self.hitbox_size1)

    def draw(self, surf, screen, color=(255, 0, 0, 200)):
        # pygame.draw.rect(surf, color, (self.character_pos[0]-self.hitbox_size/2, self.character_pos[1]-self.hitbox_size/2, self.hitbox_size, self.hitbox_size),8)
        surf.blit(self.character_image, (self.character_pos1[0] - 27, self.character_pos1[1] - 38))
        screen.blit(surf, (0, 0))

    def collision(self, mask, platform):
        touching = False
        self.phisical_hitbox_points = [[self.character_pos1[0] - self.hitbox_size1 / 2, self.character_pos1[1]],
                                       [self.character_pos1[0], self.character_pos1[1] - self.hitbox_size1 / 2],
                                       [self.character_pos1[0], self.character_pos1[1] + self.hitbox_size1 / 2],
                                       [self.character_pos1[0] + self.hitbox_size1 / 2, self.character_pos1[1]]]
        for i, cords in enumerate(self.phisical_hitbox_points):
            pos_in_mask = cords[0] - mask.rect.x, cords[1] - mask.rect.y
            touching = mask.rect.collidepoint(*cords) and mask.mask.get_at(pos_in_mask)
            if touching:
                if i == 0:
                    # касание левой частью хитбокса
                    self.is_touching1[0] = True
                if i == 3:
                    # касание правой частью
                    self.is_touching1[1] = True
                if i == 1:
                    # касание верхней частью
                    self.is_touching1[2] = True
                if i == 2:
                    # касание нижней
                    self.is_touching1[3] = True
            else:
                if i == 0:
                    # касание левой частью хитбокса
                    self.is_touching1[0] = False
                if i == 3:
                    # касание правой частью
                    self.is_touching1[1] = False
                if i == 1:
                    # касание верхней частью
                    self.is_touching1[2] = False
                if i == 2:
                    # касание нижней
                    self.is_touching1[3] = False

        if platform.collision(self.hitbox1):
            self.is_touching1[3] = True
        if self.is_touching:
            color = (255, 255, 255)
        else:
            color = (255, 0, 0, 200)
        return color
