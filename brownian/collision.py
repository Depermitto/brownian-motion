from .entity import Entity
from typing import Tuple
from numpy import sqrt


class Collision:
    """
    A collection of static methods that are used in collision resolution.
    """
    @staticmethod
    def static_static(c1: Entity, c2: Entity, threshold: int = 0) -> None:
        """Performs static-static collision check
        and adjusts positions of colliding entities."""

        distsq = (c2.x - c1.x) ** 2 + (c2.y - c1.y) ** 2
        # if centers are the same we set distance to a very small number
        distsq = max(distsq, 1e-6)
        radii = (c1.radius + c2.radius) ** 2
        if distsq + threshold**2 < radii:
            d = sqrt(distsq)
            midpointx = (c1.x + c2.x) / 2
            midpointy = (c1.y + c2.y) / 2

            c1.x = midpointx + c1.radius * (c1.x - c2.x) / d
            c1.y = midpointy + c1.radius * (c1.y - c2.y) / d
            c2.x = midpointx + c2.radius * (c2.x - c1.x) / d
            c2.y = midpointy + c2.radius * (c2.y - c1.y) / d

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
                c1.x + c1.vx,
                c1.y + c1.vy,
                c1.x,
                c1.y,
                c2.x,
                c2.y,
            )
            closestdistsq = (c2.x - sx) ** 2 + (c2.y - sy) ** 2
            backdist = sqrt(radiisq - closestdistsq)
            movement_vector_length = sqrt(c1.vx**2 + c1.vy**2)
            collisionx = sx - backdist * (c1.vx / movement_vector_length)
            collisiony = sy - backdist * (c1.vy / movement_vector_length)

            collisiondist = sqrt((c2.x - collisionx) ** 2 + (c2.y - collisiony) ** 2)

            nx = (c2.x - collisionx) / collisiondist
            ny = (c2.y - collisiony) / collisiondist
            p = 2 * (c1.vx * nx + c1.vy * ny) / (c1.m + c2.m)

            c1.vx = c1.vx - p * c1.m * nx - p * c2.m * nx
            c1.vy = c2.vy - p * c1.m * ny - p * c2.m * ny

    @staticmethod
    def dynamic_dynamic(c1: Entity, c2: Entity) -> None:
        """Performs dynamic-dynamic collision check and resolves colliding entities.
        This function assumes that `c1` and `c2` are both dynamics entities that have
        *already* called the `move` method."""
        distsq = (c2.x - c1.x) ** 2 + (c2.y - c1.y) ** 2
        radiisq = (c1.radius + c2.radius) ** 2
        if distsq < radiisq:
            sx, sy = Collision._closest_point_on_line(
                c1.x + c1.vx,
                c1.y + c1.vy,
                c1.x,
                c1.y,
                c2.x,
                c2.y,
            )
            closestdistsq = (c2.x - sx) ** 2 + (c2.y - sy) ** 2
            backdist = sqrt(radiisq - closestdistsq)
            movement_vector_length = sqrt(c1.vx**2 + c1.vy**2)
            collision1x = sx - backdist * (c1.vx / movement_vector_length)
            collision1y = sy - backdist * (c1.vy / movement_vector_length)

            sx, sy = Collision._closest_point_on_line(
                c1.x + c1.vx,
                c1.y + c1.vy,
                c1.x,
                c1.y,
                c2.x,
                c2.y,
            )
            closestdistsq = (c1.x - sx) ** 2 + (c1.y - sy) ** 2
            backdist = sqrt(radiisq - closestdistsq)
            movement_vector_length = sqrt(c2.vx**2 + c2.vy**2)
            collision2x = sx - backdist * (c2.vx / movement_vector_length)
            collision2y = sy - backdist * (c2.vy / movement_vector_length)

            del sx, sy, closestdistsq, backdist, movement_vector_length

            d = sqrt(
                (collision1x - collision2x) ** 2 + (collision1y - collision2y) ** 2
            )
            nx = (collision2x - collision1x) / d
            ny = (collision2y - collision1y) / d
            p = 2 * (c1.vx * nx + c1.vy * ny - c2.vx * nx - c2.vy * ny) / (c1.m + c2.m)

            c1.vx -= p * c1.m * nx
            c1.vy -= p * c1.m * ny
            c2.vx += p * c2.m * nx
            c2.vy += p * c2.m * ny

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
