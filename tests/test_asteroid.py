import pytest

from asteroid import Asteroid
from robot import Robot, Bearing


@pytest.fixture
def asteroid():
    return Asteroid(5, 5)


def test_asteroid_created_with_correct_size_and_without_robots(asteroid):
    assert asteroid.size_x == 5
    assert asteroid.size_y == 5
    assert asteroid.robots == []


@pytest.mark.parametrize(
    "x, y, error_message",
    [
        (-1, 5, "Invalid x coordinate for the size of the asteroid, can't be negative"),
        (5, -5, "Invalid y coordinate for the size of the asteroid, can't be negative"),
    ],
)
def test_value_error_raised_when_initializing_invalid_x_y_size_for_asteroid(
    x, y, error_message
):
    with pytest.raises(ValueError, match=error_message):
        Asteroid(x, y)
