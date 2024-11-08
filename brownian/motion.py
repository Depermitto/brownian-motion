import numpy as np


class BrownianMotion:
    @staticmethod
    def static(dt: float, mu: float = 0, sigma: float = 1) -> float:
        return 0

    @staticmethod
    def standard(dt: float, mu: float = 0, sigma: float = 1) -> float:
        return np.sqrt(dt) * np.random.randn()

    @staticmethod
    def drift(dt: float, mu: float = 0, sigma: float = 1) -> float:
        return mu * dt + sigma * np.sqrt(dt) * np.random.randn()

    @staticmethod
    def geometric(dt: float, mu: float = 0, sigma: float = 1) -> float:
        return (mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * np.random.randn()
