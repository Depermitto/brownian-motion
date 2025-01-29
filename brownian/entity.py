import pygame
from pygame.locals import *

from .motion import BrownianMotion

# typing imports
from typing import Tuple, Callable


class Entity(pygame.sprite.Sprite):
    def __init__(
        self,
        center: Tuple[float | int, float | int],
        radius: int = 10,
        color: Tuple[int, int, int] = (255, 255, 255),
        m: float = 1,
        mu: float = 0,
        sigma: float = 1,
        x_motion: Callable = BrownianMotion.standard,
        y_motion: Callable = BrownianMotion.standard,
        movement_multiplier: float = 10,
        damp: float = 0.75,
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

        # velocity
        self.vx: float = 0
        self.vy: float = 0

        # other elements
        self.m = m
        self._p = movement_multiplier
        self.damp = damp

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def move(self, dt: float):
        self.vx += self._x_step(dt, self._mu, self._sigma) * self._p
        self.vy += self._y_step(dt, self._mu, self._sigma) * self._p

        self.x += self.vx
        self.y += self.vy

        self.vx *= self.damp
        self.vy *= self.damp
