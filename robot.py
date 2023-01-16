from enum import Enum


class Bearing(Enum):
    """
    An enumeration class that defines the possible bearings a robot can have.
    """

    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"


class Movement(Enum):
    """
    An enumeration class that defines the possible movements a robot can make.
    """

    MOVE_FORWARD = "move-forward"
    TURN_LEFT = "turn-left"
    TURN_RIGHT = "turn-right"


class CommandType(Enum):
    """
    An enumeration class that defines the possible types of commands that can be executed.
    """

    NEW_ASTEROID = "new-asteroid"
    NEW_ROBOT = "new-robot"
    MOVE = "move"


class Robot:
    """
    A class representing a robot that can be sent to an asteroid.
    The class has the following properties:
    - x: the x-coordinate of the robot's position
    - y: the y-coordinate of the robot's position
    - bearing: the current bearing of the robot (north, south, east, or west)
    - x_boundary: the maximum x-coordinate the robot can have
    - y_boundary: the maximum y-coordinate the robot can have
    The class has the following methods:
    - move: moves the robot forward or turns it left or right
    - __str__: returns a string representation of the robot's current position and bearing
    """

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

    def move(self, movement: Movement) -> None:
        if movement == Movement.MOVE_FORWARD:
            if self.bearing == Bearing.NORTH:
                self.y = min(self.y_boundary, self.y + 1)
            elif self.bearing == Bearing.SOUTH:
                self.y = max(0, self.y - 1)
            elif self.bearing == Bearing.EAST:
                self.x = min(self.x_boundary, self.x + 1)
            elif self.bearing == Bearing.WEST:
                self.x = max(0, self.x - 1)
        else:
            self.bearing = Robot.BEARING_DIRECTIONS[self.bearing][movement]

    def __str__(self) -> str:
        return f"Robot at position ({self.x}, {self.y}), bearing {self.bearing.value}"
