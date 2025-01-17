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
        self.size = 1280, 720
        self._display_surf = pygame.display.set_mode(
            self.size, pygame.RESIZABLE | pygame.HWSURFACE | pygame.DOUBLEBUF
        )
        self._is_running = True
        self._background_color = background_color
        self._curr_scene: Scene | None = None
        self._menu = Menu(self.select_scene, size=self.size)

    def register_scene(self, scene: Scene) -> None:
        self._menu.register_scene(scene)

    def select_scene(self, title, scene: Scene):
        if scene is None:
            return
        self._curr_scene = scene
        self._menu.close_menu()

    def on_event(self, event) -> None:
        match event.type:
            case pygame.QUIT:
                self._is_running = False
            case pygame.VIDEORESIZE:
                self.size = (event.w, event.h)
                self._display_surf = pygame.display.set_mode(
                    self.size, pygame.RESIZABLE | pygame.HWSURFACE | pygame.DOUBLEBUF
                )
                print("resize")
                self._menu.change_size(self.size)
            case pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                print(f"'{key}' pressed")
                if pygame.key.key_code(key) == pygame.K_ESCAPE:
                    self._menu.enable()
                    self._menu.run(self._display_surf)
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
            self._menu.run(self._display_surf)

        assert self._curr_scene is not None

        clock = pygame.time.Clock()
        while self._is_running:
            dt: float = clock.tick(60) / 1000  # convert to seconds

            for event in pygame.event.get():
                self.on_event(event)
            self._curr_scene.on_loop(dt, (0, 0, *pygame.display.get_window_size()))
            self._curr_scene.on_render(self._display_surf)
        self.on_cleanup()
