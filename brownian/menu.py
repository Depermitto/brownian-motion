import pygame
import pygame_menu
# typing imports
from typing import Tuple
from .scene import Scene

import pygame_menu.events

class Menu(pygame_menu.Menu):
    def __init__(self, callback: callable, title: str="Choose scene", size: Tuple[int,int]=(400,300), 
                 theme: pygame_menu.Theme=pygame_menu.themes.THEME_DARK) -> None:
        super(Menu, self).__init__(title, size[0], size[1], theme=theme, onclose=pygame_menu.events.CLOSE)
        self._callback: callable = callback
        self.add.button("Quit",pygame_menu.events.EXIT)

    def register_scene(self, scene: Scene) -> None:
        self.add.button(scene.get_name(), self._callback, scene)

    def run(self) -> None:
        self.mainloop()