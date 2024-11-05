import numpy as np
import brownian

def main():
    print("Hello, FO!")
    app = brownian.App()
    e1 = brownian.Entity((200,200), 50)
    e2 = brownian.Entity((300,300), 75, (100, 200, 255))
    app.register_entity(e1)
    app.register_entity(e2)
    app.run()
    print("Goodbye!")


if __name__ == "__main__":
    main()
