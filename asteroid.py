class Asteroid:
    def __init__(self, size_x: int, size_y: int) -> None:
        self.size_x = size_x
        self.size_y = size_y
        self.robots = []

    @property
    def size_x(self) -> int:
        return self._size_x

    @size_x.setter
    def size_x(self, value: int):
        if value < 0:
            raise ValueError(
                "Invalid x coordinate for the size of the asteroid, can't be negative"
            )
        self._size_x = value

    @property
    def size_y(self) -> int:
        return self._size_y

    @size_y.setter
    def size_y(self, value: int) -> None:
        if value < 0:
            raise ValueError(
                "Invalid y coordinate for the size of the asteroid, can't be negative"
            )
        self._size_y = value

    def add_robot(self):
        pass


