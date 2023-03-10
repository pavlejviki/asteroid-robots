class Asteroid:
    """
    A class representing an asteroid that can be created.
    The class has the following properties:
    - size_x: the x-coordinate of the asteroid's size
    - size_y: the y-coordinate of the asteroid's size
    - robots: a list of robots on the asteroid
    The class has the following methods:
    - add_robot: adds a new robot to the asteroid
    - __str__: returns a string representation of the asteroid's size and the number of robots on it
    """

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
    def size_y(self, value: int):
        if value < 0:
            raise ValueError(
                "Invalid y coordinate for the size of the asteroid, can't be negative"
            )
        self._size_y = value

    def add_robot(self, robot) -> None:
        self.robots.append(robot)

    def __str__(self) -> str:
        return f"Asteroid of size ({self.size_x}, {self.size_y}) with {len(self.robots)} robots on it."
