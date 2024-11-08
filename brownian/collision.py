from .entity import Entity
from typing import Tuple
from numpy import sqrt


class Collision:
    @staticmethod
    def static_static(c1: Entity, c2: Entity, threshold: int = 0) -> None:
        """Performs static-static collision check
        and adjusts positions of colliding entities."""

        distsq = (c2.x - c1.x) ** 2 + (c2.y - c1.y) ** 2
        # if centers are the same we set distance to a very small number
        distsq = max(distsq, 1e-6)
        radii = (c1.radius + c2.radius) ** 2
        if distsq + threshold < radii:
            dist = sqrt(distsq)
            midpointx = (c1.x + c2.x) / 2
            midpointy = (c1.y + c2.y) / 2

            c1.x = midpointx + c1.radius * (c1.x - c2.x) / dist
            c1.y = midpointy + c1.radius * (c1.y - c2.y) / dist
            c2.x = midpointx + c2.radius * (c2.x - c1.x) / dist
            c2.y = midpointy + c2.radius * (c2.y - c1.y) / dist

    @staticmethod
    def dynamic_static(c1: Entity, c2: Entity) -> None:
        """Performs dynamic-static collision check and resolves colliding entities.
        This function assumes that `c1` is a dynamic entity that has
        *already* called the `move` method, and that `c2` isn't and hasn't."""

        distsq = (c2.x - c1.x) ** 2 + (c2.y - c1.y) ** 2
        radiisq = (c1.radius + c2.radius) ** 2
        if distsq < radiisq:
            # let (s) be the closest point on line between moving c1 and non-moving c2
            sx, sy = Collision._closest_point_on_line(
                c1.x - c1.dx, c1.y - c1.dy, c1.x, c1.y, c2.x, c2.y
            )
            closestdistsq = (c2.x - sx) ** 2 + (c2.y - sy) ** 2
            backdist = sqrt(radiisq - closestdistsq)
            movement_vector_length = sqrt(c1.dx**2 + c1.dy**2)
            collisionx = sx - backdist * (c1.dx / movement_vector_length)
            collisiony = sy - backdist * (c1.dy / movement_vector_length)

            collisiondist = sqrt((c2.x - collisionx) ** 2 + (c2.y - collisiony) ** 2)

            nx = (c2.x - collisionx) / collisiondist
            ny = (c2.y - collisiony) / collisiondist
            p = 2 * (c1.dx * nx + c1.dy * ny) / (c1.m + c2.m)

            c1.x += c1.dx - p * c1.m * nx - p * c2.m * nx
            c1.y += c1.dy - p * c1.m * ny - p * c2.m * ny

    @staticmethod
    def bounding_box(c: Entity, bounds: Tuple[int, int, int, int]) -> None:
        left, top, right, bot = bounds

        # pmjial math. It works just trust me bro.
        if c.x - c.radius < left:
            c.x = 2 * left + 2 * c.radius - c.x
        if c.y - c.radius < top:
            c.y = 2 * top + 2 * c.radius - c.y
        if c.x + c.radius > right:
            c.x = 2 * right - 2 * c.radius - c.x
        if c.y + c.radius > bot:
            c.y = 2 * bot - 2 * c.radius - c.y

    @staticmethod
    def _closest_point_on_line(
        lx1: float,
        ly1: float,
        lx2: float,
        ly2: float,
        x: float,
        y: float,
    ) -> Tuple[float, float]:
        A1: float = ly2 - ly1
        B1: float = lx1 - lx2
        det: float = A1 * A1 - -B1 * B1
        if det == 0:
            return (x, y)
        else:
            C1: float = (ly2 - ly1) * lx1 + (lx1 - lx2) * ly1
            C2: float = -B1 * x + A1 * y
            return ((A1 * C1 - B1 * C2) / det, (A1 * C2 - -B1 * C1) / det)
