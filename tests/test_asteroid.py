import pytest

from asteroid import Asteroid


@pytest.fixture
def asteroid():
    return Asteroid(5, 5)


def test_asteroid_created_with_correct_size_and_without_robots(robot):
    assert asteroid.size_x == 5
    assert asteroid.size_y == 5
    assert asteroid.robots == []
