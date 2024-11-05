import pygame
from pygame.locals import *
# typing imports
from typing import Tuple

class Entity(pygame.sprite.Sprite):
    def __init__(self, center: Tuple[int,int], radius: int=10, color: Tuple[int,int,int]=(255,255,255)):
        super(Entity, self).__init__()
        if type(radius) != int or radius <= 0:
            raise ValueError("Radius must be a positive integer")
        if any(not (0 <= value <= 255) for value in color):
            raise ValueError("Color values must be RGB between 0-255")
        self.x, self.y = center
        self.color = color
        self.radius = radius

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def move(self):
        # TODO: implement
        from random import randint
        self.x += randint(-1,1)
        self.y += randint(-1,1)
