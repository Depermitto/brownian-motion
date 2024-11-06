import numpy as np


class BrownianMotion:
    def static(x: float | int, dt: float, mu: float = 0, sigma: float = 1) -> float:
        return 0

    def standard(x: float | int, dt: float, mu: float = 0, sigma: float = 1) -> float:
        return np.sqrt(dt) * np.random.randn()

    def drift(x: float | int, dt: float, mu: float = 0, sigma: float = 1) -> float:
        return mu * dt + sigma * np.sqrt(dt) * np.random.randn()

    def geometric(x: float | int, dt: float, mu: float = 0, sigma: float = 1) -> float:
        if x == 0:
            x = 1  # prevent being stuck
        return x * (
            np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * np.random.randn())
            - 1
        )
