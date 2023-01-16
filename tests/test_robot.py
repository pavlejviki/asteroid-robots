import pytest
from robot import Robot


@pytest.fixture
def robot():
    robot = Robot(2, 2, "north", 5, 5)
    return robot


def test_robot_created_with_correct_initial_state(robot):
    assert robot.x == 2
    assert robot.y == 2
    assert robot.bearing == "north"
    assert robot.x_boundary == 5
    assert robot.y_boundary == 5
    assert isinstance(robot, Robot)


def test_value_error_raised_when_initializing_x_y_coordinate_outside_boundary():
    with pytest.raises(ValueError, match="Invalid x coordinate for robot, must be within boundaries"):
        Robot(6, 2, "north", 5, 5)
