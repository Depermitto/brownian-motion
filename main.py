import brownian
import brownian.examples


def main():
    print("Hello, FO!")
    app = brownian.App()
    app.register_scene(brownian.examples.two_entities())
    app.register_scene(brownian.examples.trailing_entity())
    app.register_scene(brownian.examples.different_movements())
    app.register_scene(brownian.examples.collision_test())
    app.run()
    print("Goodbye!")


if __name__ == "__main__":
    main()
