import pygame
from pygame.locals import *  # type: ignore
from .collision import Collision

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
                match (c1.dx, c1.dy, c2.dx, c2.dy):
                    case (0, 0, 0, 0):
                        Collision.static_static(c1, c2, int(c1.radius + c2.radius / 4))
                    case (0, 0, _, _):
                        Collision.dynamic_static(c2, c1)
                    case (_, _, 0, 0):
                        Collision.dynamic_static(c1, c2)
                    case _:
                        Collision.dynamic_dynamic(c1, c2)
            Collision.bounding_box(c1, bounding_box)

    def on_render(self, surface) -> None:
        surface.fill(self._background_color)
        for entity in self._entities:
            entity.draw(surface)
        pygame.display.update()
