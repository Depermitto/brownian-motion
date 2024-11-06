import pygame
import numpy as np
from pygame.locals import *

# typing imports
from typing import Tuple, List
from .entity import Entity


class Scene:
    def __init__(
        self, name: str, background_color: Tuple[int, int, int] = (21, 32, 43)
    ) -> None:
        self.name = name
        self._background_color = background_color
        self._entities: List[Entity] = []

    def get_name(self) -> str:
        return self.name

    def register_entity(self, entity: Entity) -> None:
        self._entities.append(entity)

    def on_loop(self, dt: float) -> None:
        for c1 in self._entities:
            from random import randint

            c1.vx += randint(-10, 10)
            c1.vy += randint(-10, 10)

            for c2 in self._entities:
                if c2 == c1:
                    continue

                d = np.sqrt((c2.x - c1.x) ** 2 + (c2.y - c1.y) ** 2)
                if d >= c1.radius + c2.radius or d == 0:
                    continue

                # dynamic-dynamic collision
                nx = (c2.x - c1.x) / d
                ny = (c2.y - c1.y) / d
                p = (
                    2
                    * (c1.vx * nx + c1.vy * ny - c2.vx * nx - c2.vy * ny)
                    / (c1.m + c2.m)
                )

                c1.vx -= p * c1.m * nx
                c1.vy -= p * c1.m * ny
                c2.vx -= p * c2.m * nx
                c2.vy -= p * c2.m * ny

            c1.move(dt)

    def on_render(self, surface) -> None:
        surface.fill(self._background_color)
        for entity in self._entities:
            entity.draw(surface)
        pygame.display.update()
