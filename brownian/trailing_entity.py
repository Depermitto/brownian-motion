import pygame

from .entity import Entity
from .motion import BrownianMotion

# typing imports
from typing import Tuple, Callable


class TrailingEntity(Entity):
    """
    A class representing an entity that leaves a trail behind it showing it's movement pattern.
    """
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
        trail_color: Tuple[int, int, int] = (255, 255, 255),
        damp: float = 0.75,
    ):
        super().__init__(
            center,
            radius,
            color,
            m,
            mu,
            sigma,
            x_motion,
            y_motion,
            movement_multiplier,
            damp,
        )
        self.trail: list[Tuple[float, float]] = [(self.x, self.y)]
        self.trail_color: Tuple[int, int, int] = trail_color

    def draw(self, surface):  # type: ignore
        self.trail.append((self.x, self.y))
        pygame.draw.lines(
            surface,
            self.trail_color,
            False,
            self.trail,
            width=max(self.radius // 10, 2),
        )
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
