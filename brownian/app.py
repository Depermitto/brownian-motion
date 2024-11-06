import pygame
from pygame.locals import *

# typing imports
from typing import Tuple, List
from .scene import Scene
from .menu import Menu


class App:
    def __init__(self, background_color: Tuple[int, int, int] = (21, 32, 43)) -> None:
        pygame.init()
        pygame.display.set_caption("Brownian motion simulation")
        self.size = self.width, self.height = 1600, 800
        self._display_surf = pygame.display.set_mode(
            self.size, pygame.RESIZABLE | pygame.HWSURFACE | pygame.DOUBLEBUF
        )
        self._is_running = True
        self._background_color = background_color
        self._curr_scene = None
        self._menu = Menu(self.select_scene, size=(1600, 800))

    def register_scene(self, scene: Scene) -> None:
        self._menu.register_scene(scene)

    def select_scene(self, title, scene: Scene):
        if scene is None:
            return
        self._curr_scene = scene
        self._menu.close()

    def on_event(self, event) -> None:
        match event.type:
            case pygame.QUIT:
                self._is_running = False
            case pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                print(f"'{key}' pressed")
                if pygame.key.key_code(key) == pygame.K_ESCAPE:
                    self._menu.enable()
                    self._menu.mainloop(self._display_surf)
            case pygame.KEYUP:
                key = pygame.key.name(event.key)
                print(f"'{key}' released")
            case pygame.MOUSEBUTTONDOWN:
                mb = pygame.mouse.get_pressed()
                x, y = pygame.mouse.get_pos()
                btn = ""
                if mb[0]:
                    btn = "Left"
                elif mb[2]:
                    btn = "Right"
                print(f"{btn} mouse button pressed at ({x},{y})")

    def on_cleanup(self) -> None:
        pygame.quit()

    def run(self) -> None:
        if self._curr_scene is None:
            self._menu.mainloop(self._display_surf)

        while self._is_running:
            for event in pygame.event.get():
                self.on_event(event)
            self._curr_scene.on_loop()
            self._curr_scene.on_render(self._display_surf)
        self.on_cleanup()
