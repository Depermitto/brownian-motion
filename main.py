import numpy as np
import pygame
import brownian


def get_scene_duo() -> brownian.Scene:
    s = brownian.Scene("Duo")
    e1 = brownian.Entity((200, 200), 50)
    e2 = brownian.Entity((300, 300), 75, (100, 200, 255))
    s.register_entity(e1)
    s.register_entity(e2)
    return s


def get_scene_single_guy() -> brownian.Scene:
    s = brownian.Scene("Single guy")
    e = brownian.TrailingEntity(
        (300, 200),
        30,
        (255, 255, 0),
        x_motion=brownian.BrownianMotion.geometric,
        y_motion=brownian.BrownianMotion.geometric,
        mu=18,
        sigma=6,
    )
    s.register_entity(e)
    return s


def get_scene_motion_test() -> brownian.Scene:
    s = brownian.Scene("Different movement options")
    stat = brownian.Entity(
        (320, 400),
        50,
        (0, 0, 255),
        x_motion=brownian.BrownianMotion.static,
        y_motion=brownian.BrownianMotion.static,
    )
    std = brownian.Entity(
        (640, 400),
        50,
        (0, 255, 0),
        x_motion=brownian.BrownianMotion.standard,
        y_motion=brownian.BrownianMotion.standard,
    )
    dr = brownian.Entity(
        (960, 400),
        50,
        (255, 0, 0),
        x_motion=brownian.BrownianMotion.drift,
        y_motion=brownian.BrownianMotion.drift,
        mu=3,
        sigma=7,
    )
    geo = brownian.Entity(
        (1280, 400),
        50,
        (255, 255, 255),
        x_motion=brownian.BrownianMotion.geometric,
        y_motion=brownian.BrownianMotion.geometric,
        mu=3,
        sigma=7,
    )
    s.register_entity(stat)
    s.register_entity(std)
    s.register_entity(dr)
    s.register_entity(geo)
    return s


def get_scene_collision_test() -> brownian.Scene:
    maxx, maxy = pygame.display.get_window_size()

    s = brownian.Scene("Collision test")
    s.register_entity(
        brownian.Entity(
            center=(maxx / 2, maxy / 2),
            radius=75,
            color=(100, 200, 255),
            m=1,
            movement_multiplier=0.01,
        )
    )

    entities_n = 150
    x = np.random.randint(0, maxx, entities_n)
    y = np.random.randint(0, maxy, entities_n)
    for i in range(entities_n):
        s.register_entity(
            brownian.Entity(
                center=(x[i], y[i]),
                radius=20,
                m=60,
                movement_multiplier=50,
            )
        )

    return s


def main():
    print("Hello, FO!")
    app = brownian.App()
    app.register_scene(get_scene_duo())
    app.register_scene(get_scene_single_guy())
    app.register_scene(get_scene_motion_test())
    app.register_scene(get_scene_collision_test())
    app.run()
    print("Goodbye!")


if __name__ == "__main__":
    main()
