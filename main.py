import numpy as np
import pygame
import brownian


def get_scene1() -> brownian.Scene:
    s = brownian.Scene("Test scene 1")
    e1 = brownian.Entity((200, 200), 50)
    e2 = brownian.Entity((300, 300), 75, (100, 200, 255))
    s.register_entity(e1)
    s.register_entity(e2)
    return s


def get_scene2() -> brownian.Scene:
    s = brownian.Scene("Test scene 2")
    e = brownian.Entity((300, 200), 100, (255, 255, 0))
    s.register_entity(e)
    return s


def get_scene_collision_test(entities_n: int = 30) -> brownian.Scene:
    maxx, maxy = pygame.display.get_window_size()

    s = brownian.Scene("Collision test")
    r1 = brownian.Entity((maxx / 2, maxy / 2), 75, (100, 200, 255))
    s.register_entity(r1)

    x = np.random.randint(0, maxx, entities_n)
    y = np.random.randint(0, maxy, entities_n)
    for i in range(entities_n):
        s.register_entity(brownian.Entity((x[i], y[i]), 50))

    return s


def main():
    print("Hello, FO!")
    app = brownian.App()
    app.register_scene(get_scene1())
    app.register_scene(get_scene2())
    app.register_scene(get_scene_collision_test())
    app.run()
    print("Goodbye!")


if __name__ == "__main__":
    main()
