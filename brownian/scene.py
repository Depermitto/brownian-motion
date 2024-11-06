import pygame
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

    def on_loop(self) -> None:
        for entity in self._entities:
            entity.move()

    def on_render(self, surface) -> None:
        surface.fill(self._background_color)
        for entity in self._entities:
            entity.draw(surface)
        pygame.display.update()
