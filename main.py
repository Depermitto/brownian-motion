import brownian


def main():
    app = brownian.App()
    app.register_scene(brownian.examples.two_entities())
    app.register_scene(brownian.examples.trailing_entity())
    app.register_scene(brownian.examples.different_movements())
    app.register_scene(brownian.examples.simulation())
    app.run()

    
if __name__ == "__main__":
    main()
