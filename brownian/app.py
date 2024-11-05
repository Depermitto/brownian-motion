import pygame
from pygame.locals import *
from typing import Tuple, List
from .entity import Entity

class App:
    def __init__(self, background_color: Tuple[int,int,int]=(21,32,43)) -> None:
        self._is_running = True
        self._display_surf = None
        self.size = self.width, self.height = 640, 400
        self._background_color = background_color
        self._entities: List[Entity] = []
    
    def on_init(self) -> None:
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._is_running = True

    def register_entity(self, entity: Entity) -> None:
        self._entities.append(entity)

    def on_event(self, event) -> None:
        if event.type == pygame.QUIT:
            self._is_running = False
        if event.type == pygame.KEYDOWN:
            key=pygame.key.name(event.key)
            print (f"'{key}' pressed")
        elif event.type == pygame.KEYUP:
            key=pygame.key.name(event.key)
            print (f"'{key}' released")
        match event.type:
            case pygame.QUIT:
                self._is_running = False
            case pygame.KEYDOWN:
                key=pygame.key.name(event.key)
                print (f"'{key}' pressed")
            case pygame.KEYUP:
                key=pygame.key.name(event.key)
                print (f"'{key}' released")
            case pygame.MOUSEBUTTONDOWN:
                mb=pygame.mouse.get_pressed()
                x,y = pygame.mouse.get_pos()
                btn = ""
                if mb[0]:
                    btn = "Left"
                elif mb[2]:
                    btn = "Right"
                print(f"{btn} mouse button pressed at ({x},{y})")
    
    def on_loop(self) -> None:
        for entity in self._entities:
            entity.move()

    def on_render(self) -> None:
        self._display_surf.fill(self._background_color)
        for entity in self._entities:
            entity.draw(self._display_surf)
        pygame.display.update()

    def on_cleanup(self) -> None:
        pygame.quit()
    
    def run(self) -> None:
        if self.on_init() == False:
            self._is_running = False

        while self._is_running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
