import pytest

from robot import Bearing
from robots import (
    execute_commands,
    generate_messages,
    print_messages,
    read_instructions,
)


def test_execute_commands_fulfils_commands_correctly():
    commands = [
        {"type": "asteroid", "size": {"x": 5, "y": 5}},
        {"type": "new-robot", "position": {"x": 1, "y": 2}, "bearing": "north"},
        {"type": "move", "movement": "turn-left"},
        {"type": "move", "movement": "move-forward"},
        {"type": "new-robot", "position": {"x": 3, "y": 3}, "bearing": "east"},
        {"type": "move", "movement": "move-forward"},
        {"type": "move", "movement": "move-forward"},
    ]
    asteroid = execute_commands(commands)
    robot = asteroid.robots[0]
    assert asteroid.size_x == 5
    assert asteroid.size_y == 5
    assert len(asteroid.robots) == 2
    assert robot.x == 0
    assert robot.y == 2
    assert robot.bearing == Bearing.WEST


@pytest.mark.parametrize(
    "bearing, movement, command_type",
    [
        ("invalid-bearing", "move", "move-forward"),
        (Bearing.NORTH, "invalid-type", "move-forward"),
        (Bearing.NORTH, "move", "invalid-movement"),
    ],
)
def test_execute_commands_raises_error_on_invalid_values(
    bearing, command_type, movement
):
    commands = [
        {"type": "new-asteroid", "size": {"x": 5, "y": 5}},
        {"type": "new-robot", "position": {"x": 1, "y": 2}, "bearing": bearing},
        {"type": command_type, "movement": movement},
    ]
    with pytest.raises(ValueError):
        execute_commands(commands)


def test_print_messages(capsys):
    commands = read_instructions("../instructions.txt")
    asteroid = execute_commands(commands)
    messages = generate_messages(asteroid)
    print_messages(messages)
    captured = capsys.readouterr()
    expected_output = (
        '{"type": "robot", "position": {"x": 1, "y": 3}, "bearing": "north"}\n{"type": "robot", '
        '"position": {"x": 5, "y": 1}, "bearing": "east"}\n'
    )
    assert captured.out == expected_output
