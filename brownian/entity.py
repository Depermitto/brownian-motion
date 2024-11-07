import pygame
from pygame.locals import *

from .motion import BrownianMotion

# typing imports
from typing import Tuple


class Entity(pygame.sprite.Sprite):
    def __init__(
        self,
        center: Tuple[int, int],
        radius: int = 10,
        color: Tuple[int, int, int] = (255, 255, 255),
        mu: float = 0,
        sigma: float = 1,
        x_motion: callable = BrownianMotion.standard,
        y_motion: callable = BrownianMotion.standard,
    ):
        pygame.sprite.Sprite.__init__(self)
        if type(radius) != int or radius <= 0:
            raise ValueError("Radius must be a positive integer")
        if any(not (0 <= value <= 255) for value in color):
            raise ValueError("Color values must be RGB between 0-255")
        # shape elements
        self.x, self.y = center
        self.color = color
        self.radius = radius
        # movement elements
        self._mu = mu
        self._sigma = sigma
        self._x_step = x_motion
        self._y_step = y_motion
        # TODO: Resolve this bs
        self.vx = 0
        self.vy = 0
        self.m = 1

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def move(self, dt: float):
        # TODO: currently multiplying by 10 so we can see the effect, possibly parametrize it ??
        self.x += self._x_step(self.x, dt, self._mu, self._sigma) * 10
        self.y += self._y_step(self.y, dt, self._mu, self._sigma) * 10
        # TODO: resolve this bs
        # self.x += self.vx * dt
        # self.y += self.vy * dt
