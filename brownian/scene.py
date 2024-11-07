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

                # static-static collision
                d = np.sqrt((c2.x - c1.x) ** 2 + (c2.y - c1.y) ** 2)
                d = max(d, 0.0001)
                if d < c1.radius + c2.radius:
                    # we were already colliding, so we need to uncollide

                    midpointx = (c1.x + c2.x) / 2
                    midpointy = (c1.y + c2.y) / 2

                    c1.x = midpointx + c1.radius * (c1.x - c2.x) / d
                    c1.y = midpointy + c1.radius * (c1.y - c2.y) / d
                    c2.x = midpointx + c2.radius * (c2.x - c1.x) / d
                    c2.y = midpointy + c2.radius * (c2.y - c1.y) / d

                    continue

                # dynamic-static collision (for now...)
                col1 = self._static_dynamic_collision(c1, c2)
                col2 = self._static_dynamic_collision(c2, c1)
                if col1 is not None and col2 is not None:
                    print(col1, col2)
                    c1x, c1y = col1
                    c2x, c2y = col2

                    nx = (c2x - c1x) / d
                    ny = (c2y - c1y) / d
                    p = (
                        2
                        * (c1.vx * nx + c1.vy * ny - c2.vx * nx - c2.vy * ny)
                        / (c1.m + c2.m)
                    )

                    c1.vx -= p * c1.m * nx
                    c1.vy -= p * c1.m * ny
                    c2.vx -= p * c2.m * nx
                    c2.vy -= p * c2.m * ny

                    continue

            c1.move()

    def on_render(self, surface) -> None:
        surface.fill(self._background_color)
        for entity in self._entities:
            entity.draw(surface)
        pygame.display.update()

    @staticmethod
    def _closest_point_on_line(
        lx1: float,
        lx2: float,
        ly1: float,
        ly2: float,
        x: float,
        y: float,
    ) -> Tuple[int, int]:
        A1: float = ly2 - ly1
        B1: float = lx1 - lx2
        det: float = A1 * A1 - -B1 * B1
        if det == 0:
            return (x, y)
        else:
            C1: float = (ly2 - ly1) * lx1 + (lx1 - lx2) * ly1
            C2: float = -B1 * x + A1 * y
            return ((A1 * C1 - B1 * C2) / det, (A1 * C2 - -B1 * C1) / det)

    @staticmethod
    def _static_dynamic_collision(c1: Entity, c2: Entity) -> Tuple[int, int] | None:
        dx, dy = Scene._closest_point_on_line(
            c1.x,
            c1.y,
            c1.x + c1.vx,
            c1.y + c1.vy,
            c2.x,
            c2.y,
        )
        d_squared = (c2.x - dx) ** 2 + (c2.y - dy) ** 2
        if d_squared <= (c1.radius + c2.radius) ** 2:
            # we will collide, as such we need to alter our course to prevent this disaster
            d_back = np.sqrt((c1.radius + c2.radius) ** 2 - d_squared)
            mv_len = np.sqrt(c1.vx**2 + c1.vy**2)
            colx = dx - d_back * (c1.vx / mv_len)
            coly = dy - d_back * (c1.vy / mv_len)

            return (colx, coly)
        else:
            return None
