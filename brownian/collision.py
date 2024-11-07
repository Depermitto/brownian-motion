from .entity import Entity
from typing import Tuple
from numpy import sqrt


class Collision:
    @staticmethod
    def static_static(c1: Entity, c2: Entity) -> None:
        """Performs static-static collision check
        and adjusts positions of colliding entities."""

        d = sqrt((c2.x - c1.x) ** 2 + (c2.y - c1.y) ** 2)
        d = max(d, 0.0001)  # if centers are the same, should happen very rarely
        if d < c1.radius + c2.radius:
            # we were already colliding, so we need to uncollide

            midpointx = (c1.x + c2.x) / 2
            midpointy = (c1.y + c2.y) / 2

            c1.x = midpointx + c1.radius * (c1.x - c2.x) / d
            c1.y = midpointy + c1.radius * (c1.y - c2.y) / d
            c2.x = midpointx + c2.radius * (c2.x - c1.x) / d
            c2.y = midpointy + c2.radius * (c2.y - c1.y) / d

    @staticmethod
    def static_dynamic(c1: Entity, c2: Entity) -> None:
        """Performs static-dynamic collision check
        and adjusts movement vector of future colliding entities."""
        distx, disty = Collision._closest_point_on_line(
            c1.x, c1.y, c1.x + c1.dx, c1.y + c1.dy, c2.x, c2.y
        )
        distsq = (c2.x - distx) ** 2 + (c2.y - disty) ** 2
        radiisq = (c1.radius + c2.radius) ** 2
        if distsq < radiisq:
            backdist = sqrt(radiisq - distsq)
            movement_vector_length = sqrt(c1.dx * c1.dx + c1.dy * c1.dy)
            collisionx = distx - backdist * (c1.dx / movement_vector_length)
            collisiony = disty - backdist * (c1.dy / movement_vector_length)
            collisiondist = sqrt((c2.x - collisionx) ** 2 + (c2.y - collisiony) ** 2)

            nx = (c2.x - collisionx) / collisiondist
            ny = (c2.y - collisiony) / collisiondist
            p = 2 * (c1.dx * nx + c1.dy * ny) / (c1.m + c2.m)

            c1.dx = c1.dx - p * c1.m * nx - p * c2.m * nx
            c1.dy = c1.dy - p * c1.m * ny - p * c2.m * ny

    @staticmethod
    def _closest_point_on_line(
        lx1: float,
        lx2: float,
        ly1: float,
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
