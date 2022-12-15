# направление
import pygame
import math
v = (1, 1)
r = 5
EMBIANT_COLOR = (255, 247, 0, 230)
REFLECT_COLOR = (237, 204, 38, 220)

def find_light_collision(v, mouse_pos, step, mask):
    if step == 0:
        return mouse_pos
    for i in range(5, 400, step):
        cords = (mouse_pos[0] + v[0]*i, mouse_pos[1] + v[1]*i)
        pos_in_mask = cords[0] - mask.rect.x, cords[1] - mask.rect.y
        touching = mask.rect.collidepoint(*cords) and mask.mask.get_at(pos_in_mask)
        if touching:
            prev_cords = mouse_pos[0] + v[0]*(i-2*step), mouse_pos[1] + v[1]*(i-2*step)
            return find_light_collision(v, prev_cords, step//2, mask)
    return mouse_pos[0] + v[0]*400, mouse_pos[1] + v[1]*400

def cast_light_line(Surface2draw, v,  mouse_pos, mask, color, step=10):
    cords = find_light_collision(v, mouse_pos, step, mask)
    pygame.draw.line(Surface2draw, color, (mouse_pos[0], mouse_pos[1]), cords, 4)
    # pygame.draw.circle(Surface2draw, REFLECT_COLOR, cords, 6)

def cast_all_lights(Surface2draw, mouse_pos, mask, color):
    for a in range(0, 36000,15):
        v = (math.sin(a/(2*math.pi/100)), math.cos(a/(2*math.pi/100)))
        cast_light_line(Surface2draw, v,  mouse_pos, mask, color)
