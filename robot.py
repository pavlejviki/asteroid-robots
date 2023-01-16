class Robot:
    def __init__(
        self, x: int, y: int, bearing: str, x_boundary: int, y_boundary: int
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
