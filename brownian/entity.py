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
    ):
        pygame.sprite.Sprite.__init__(self)
        if type(radius) != int or radius <= 0:
            raise ValueError("Radius must be a positive integer")
        if any(not (0 <= value <= 255) for value in color):
            raise ValueError("Color values must be RGB between 0-255")
        # shape elements
        self.x, self.y = center
        self.dx, self.dy = 0, 0
        self.m = 1
        self.color = color
        self.radius = radius
        # movement elements
        self._mu = mu
        self._sigma = sigma
        self._x_step = x_motion
        self._y_step = y_motion

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def move_delta(self, dt: float):
        self.dx = self._y_step(self.y, dt, self._mu, self._sigma) * 10
        self.dy = self._x_step(self.x, dt, self._mu, self._sigma) * 10

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.dx = 0
        self.dy = 0

    # def move(self, dt: float):
    #     # TODO: currently multiplying by 10 so we can see the effect, possibly parametrize it ??
    #     self.x += self._y_step(self.y, dt, self._mu, self._sigma) * 10
    #     self.y += self._x_step(self.x, dt, self._mu, self._sigma) * 10
