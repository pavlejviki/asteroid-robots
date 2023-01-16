from enum import Enum


class Bearing(Enum):
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"


class Movement(Enum):
    MOVE_FORWARD = "move-forward"
    TURN_LEFT = "turn-left"
    TURN_RIGHT = "turn-right"


class CommandType(Enum):
    NEW_ASTEROID = "new-asteroid"
    NEW_ROBOT = "new-robot"
    MOVE = "move"


class Robot:
    BEARING_DIRECTIONS = {
        Bearing.NORTH: {
            Movement.TURN_LEFT: Bearing.WEST,
            Movement.TURN_RIGHT: Bearing.EAST,
        },
        Bearing.SOUTH: {
            Movement.TURN_LEFT: Bearing.EAST,
            Movement.TURN_RIGHT: Bearing.WEST,
        },
        Bearing.EAST: {
            Movement.TURN_LEFT: Bearing.NORTH,
            Movement.TURN_RIGHT: Bearing.SOUTH,
        },
        Bearing.WEST: {
            Movement.TURN_LEFT: Bearing.SOUTH,
            Movement.TURN_RIGHT: Bearing.NORTH,
        },
    }

    def __init__(
        self, x: int, y: int, bearing: Bearing, x_boundary: int, y_boundary: int
    ) -> None:
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = x
        self.y = y
        self.bearing = bearing

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value):
        if value < 0 or value > self.x_boundary:
            raise ValueError(
                "Invalid x coordinate for robot, must be within boundaries"
            )
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if value < 0 or value > self.y_boundary:
            raise ValueError(
                "Invalid y coordinate for robot, must be within boundaries"
            )
        self._y = value
