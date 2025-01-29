import numpy as np


class BrownianMotion:
    """
    A collection of static methods that are used in generating Brownian motion in different ways.
    """
    @staticmethod
    def static(dt: float, mu: float = 0, sigma: float = 1) -> float:
        """
        Simply don't move on your own.
        """
        return 1e-100

    @staticmethod
    def standard(dt: float, mu: float = 0, sigma: float = 1) -> float:
        """
        Standard implementation of Brownian motion.
        """
        return np.sqrt(dt) * np.random.randn()

    @staticmethod
    def drift(dt: float, mu: float = 0, sigma: float = 1) -> float:
        """
        Brownian motion with drift.
        """
        return mu * dt + sigma * np.sqrt(dt) * np.random.randn()

    @staticmethod
    def geometric(dt: float, mu: float = 0, sigma: float = 1) -> float:
        """
        Geometric Brownian motion.
        """
        return (mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * np.random.randn()
