import numpy as np
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


def get_scene3() -> brownian.Scene:
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
        mu=0.01,
        sigma=0.01,
    )
    s.register_entity(stat)
    s.register_entity(std)
    s.register_entity(dr)
    s.register_entity(geo)
    return s


def main():
    print("Hello, FO!")
    app = brownian.App()
    app.register_scene(get_scene1())
    app.register_scene(get_scene2())
    app.register_scene(get_scene3())
    app.run()
    print("Goodbye!")


if __name__ == "__main__":
    main()
