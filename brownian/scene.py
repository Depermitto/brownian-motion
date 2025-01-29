import pygame
import numpy as np
from pygame.locals import *
from .collision import Collision
from math import sqrt

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

    def on_loop(self, dt: float, bounding_box: Tuple[int, int, int, int]) -> None:
        for c1 in self._entities:
            c1.move(dt)
            for c2 in self._entities:
                if c1 == c2:
                    continue
                elif c1.vx == c1.vy == c2.vx == c2.vy == 0:
                    Collision.static_static(c1, c2)
                    c1.vx = np.random.rand() / 100
                    c1.vy = np.random.rand() / 100
                    c2.vx = np.random.rand() / 100
                    c2.vy = np.random.rand() / 100
                elif c1.vx == c1.vy == 0:
                    Collision.dynamic_static(c2, c1)
                elif c2.vx == c2.vy == 0:
                    Collision.dynamic_static(c1, c2)
                else:
                    Collision.dynamic_dynamic(c1, c2)
            print(sqrt(c1.vx**2 + c1.vy**2))
            Collision.bounding_box(c1, bounding_box)

    def on_render(self, surface) -> None:
        surface.fill(self._background_color)
        for entity in self._entities:
            entity.draw(surface)
        pygame.display.update()
