import pygame
import pygame_menu

# typing imports
from typing import Tuple, Callable
from .scene import Scene

import pygame_menu.events, pygame_menu.themes


class Menu(pygame_menu.Menu):
    """
    A class representing the main menu of the application. It is responsible for
    displaying the available scenes and allowing the user to choose one. 
    Can be opened by pressing ESC.
    """
    def __init__(
        self,
        callback: Callable,
        title: str = "Choose scene",
        size: Tuple[int, int] = (400, 300),
        theme: pygame_menu.Theme = pygame_menu.themes.THEME_DARK,
    ) -> None:
        super(Menu, self).__init__(
            title, size[0], size[1], theme=theme, onclose=pygame_menu.events.CLOSE
        )
        self.add.label("Press ESC to open this menu")
        self._items: list[Tuple[str, Scene | None]] = [("", None)]
        self._selector = self.add.dropselect(
            "Choose here",
            self._items,
            onchange=callback,
            placeholder_add_to_selection_box=False,
            selection_box_width=int(size[0] * 0.8),
            open_middle=True,
            selection_box_height=16,
        )
        self.add.button("Quit", pygame_menu.events.EXIT)

    def register_scene(self, scene: Scene) -> None:
        self._items.append((scene.get_name(), scene))
        self._selector.update_items(self._items)

    def change_size(self, size: Tuple[int | float, int | float]):
        self.resize(size[0], size[1])
        self._selector._selection_box_width = int(size[0] * 0.8)

    def run(self, surface) -> None:
        self._running = True
        while self._running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self._running = False
                elif event.type == pygame.VIDEORESIZE:
                    # Update the menu size on window resize
                    new_size = event.w, event.h
                    surface = pygame.display.set_mode(
                        new_size, pygame.RESIZABLE | pygame.HWSURFACE | pygame.DOUBLEBUF
                    )
                    self.change_size(new_size)
            if self.is_enabled():
                self.update(events)
                self.draw(surface)

            pygame.display.flip()

    def close_menu(self):
        self._running = False
