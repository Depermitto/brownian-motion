import numpy as np
import brownian

def get_scene1():
    s = brownian.Scene("Test scene 1")
    e1 = brownian.Entity((200,200), 50)
    e2 = brownian.Entity((300,300), 75, (100, 200, 255))
    s.register_entity(e1)
    s.register_entity(e2)
    return s

def get_scene2():
    s = brownian.Scene("Test scene 2")
    e = brownian.Entity((300, 200), 100, (255, 255, 0))
    s.register_entity(e)
    return s

def main():
    print("Hello, FO!")
    app = brownian.App()
    app.register_scene(get_scene1())
    app.register_scene(get_scene2())
    app.run()
    print("Goodbye!")


if __name__ == "__main__":
    main()
