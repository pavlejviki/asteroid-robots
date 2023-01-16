from robot import Bearing
from robots import execute_commands


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
