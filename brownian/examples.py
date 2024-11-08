from .scene import Scene
from .entity import Entity
from .trailing_entity import TrailingEntity
from .motion import BrownianMotion

import numpy as np
import pygame


def two_entities() -> Scene:
    s = Scene("Two entities")
    e1 = Entity((200, 200), 50)
    e2 = Entity((300, 300), 75, (100, 200, 255))
    s.register_entity(e1)
    s.register_entity(e2)
    return s


def trailing_entity() -> Scene:
    s = Scene("Trailing entity")
    e = TrailingEntity(
        (300, 200),
        30,
        (255, 255, 0),
        x_motion=BrownianMotion.geometric,
        y_motion=BrownianMotion.geometric,
        mu=18,
        sigma=6,
    )
    s.register_entity(e)
    return s


def different_movements() -> Scene:
    s = Scene("Different movement options")
    stat = Entity(
        (320, 400),
        50,
        (0, 0, 255),
        x_motion=BrownianMotion.static,
        y_motion=BrownianMotion.static,
    )
    std = Entity(
        (640, 400),
        50,
        (0, 255, 0),
        x_motion=BrownianMotion.standard,
        y_motion=BrownianMotion.standard,
    )
    dr = Entity(
        (960, 400),
        50,
        (255, 0, 0),
        x_motion=BrownianMotion.drift,
        y_motion=BrownianMotion.drift,
        mu=3,
        sigma=7,
    )
    geo = Entity(
        (1280, 400),
        50,
        (255, 255, 255),
        x_motion=BrownianMotion.geometric,
        y_motion=BrownianMotion.geometric,
        mu=3,
        sigma=7,
    )
    s.register_entity(stat)
    s.register_entity(std)
    s.register_entity(dr)
    s.register_entity(geo)
    return s


def collision_test() -> Scene:
    maxx, maxy = pygame.display.get_window_size()

    s = Scene("Collision test")
    s.register_entity(
        Entity(
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
            Entity(
                center=(x[i], y[i]),
                radius=20,
                m=60,
                movement_multiplier=50,
            )
        )

    return s
