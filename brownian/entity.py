import pygame
from pygame.locals import *  # type: ignore

from .motion import BrownianMotion

# typing imports
from typing import Tuple, Callable


class Entity(pygame.sprite.Sprite):
    def __init__(
        self,
        center: Tuple[float | int, float | int],
        radius: int = 10,
        color: Tuple[int, int, int] = (255, 255, 255),
        mu: float = 0,
        sigma: float = 1,
        x_motion: Callable = BrownianMotion.standard,
        y_motion: Callable = BrownianMotion.standard,
        movement_multiplier: float = 10,
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

        self.dx = 0
        """Difference between the previous position and current on x axis"""
        self.dy = 0
        """Difference between the previous position and current on y axis"""

        # other elements
        self.m = 1
        self._p = movement_multiplier

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def move(self, dt: float):
        self.dy = self._y_step(self.y, dt, self._mu, self._sigma) * self._p
        self.dx = self._x_step(self.x, dt, self._mu, self._sigma) * self._p
        self.x += self.dx
        self.y += self.dy
