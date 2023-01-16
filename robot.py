class Robot:
    def __init__(
            self, x: int, y: int, bearing: str, x_boundary: int, y_boundary: int
    ) -> None:
        self.x = x
        self.y = y
        self.bearing = bearing
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
