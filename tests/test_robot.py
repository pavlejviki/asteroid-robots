import pytest
from robot import (
    Robot,
    Bearing,
    Movement,
)


@pytest.fixture
def robot():
    robot = Robot(2, 2, Bearing.NORTH, 5, 5)
    return robot


def test_robot_created_with_correct_initial_state(robot):
    assert robot.x == 2
    assert robot.y == 2
    assert robot.bearing == Bearing.NORTH
    assert robot.x_boundary == 5
    assert robot.y_boundary == 5
    assert isinstance(robot, Robot)


@pytest.mark.parametrize(
    "x, y, error_message",
    [
        (-1, 2, "Invalid x coordinate for robot, must be within boundaries"),
        (6, 2, "Invalid x coordinate for robot, must be within boundaries"),
        (2, -1, "Invalid y coordinate for robot, must be within boundaries"),
        (2, 6, "Invalid y coordinate for robot, must be within boundaries"),
    ],
)
def test_value_error_raised_when_initializing_x_y_coordinate_outside_boundary(x, y, error_message):
    with pytest.raises(
        ValueError, match=error_message
    ):
        Robot(x, y, Bearing.NORTH, 5, 5)


def test_robot_moves_forward_correctly(robot):
    robot.move(Movement.MOVE_FORWARD)
    assert robot.x == 2
    assert robot.y == 3
    assert robot.bearing == Bearing.NORTH


def test_robot_does_not_move_outside_boundaries(robot):
    for i in range(4):
        robot.move(Movement.MOVE_FORWARD)
    assert robot.x == 2
    assert robot.y == 5


@pytest.mark.parametrize("movement, expected_bearing", [
    (Movement.TURN_RIGHT, Bearing.EAST),
    (Movement.TURN_LEFT, Bearing.WEST),
])
def test_robot_turns_to_right_direction(robot, movement, expected_bearing):
    robot.move(movement)
    assert robot.bearing == expected_bearing


def test_robot_str_method(robot):
    assert str(robot) == "Robot at position (2, 2), bearing north"
