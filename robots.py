import json
import sys

from typing import List, Dict, Generator
from asteroid import Asteroid
from robot import Robot, CommandType, Bearing, Movement


def read_instructions(instructions: str) -> List[Dict]:
    with open(instructions, "r") as file:
        commands = []
        for row in file:
            command = json.loads(row)
            commands.append(command)
    return commands


def execute_commands(commands: List[Dict]) -> Asteroid:
    new_asteroid = Asteroid(commands[0]["size"]["x"], commands[0]["size"]["y"])
    new_robot = None
    for command in commands[1:]:
        if CommandType(command["type"]) == CommandType.NEW_ROBOT:
            new_robot = Robot(
                command["position"]["x"],
                command["position"]["y"],
                Bearing(command["bearing"]),
                new_asteroid.size_x,
                new_asteroid.size_y,
            )
            new_asteroid.add_robot(new_robot)
        if CommandType(command["type"]) == CommandType.MOVE:
            new_robot.move(Movement(command["movement"]))
    return new_asteroid


def generate_messages(asteroid: Asteroid) -> Generator[str, None, None]:
    for robot in asteroid.robots:
        robot_details = {
            "type": "robot",
            "position": {"x": robot.x, "y": robot.y},
            "bearing": robot.bearing.value,
        }
        yield json.dumps(robot_details)


def print_messages(messages: Generator[str, None, None]) -> None:
    for message in messages:
        print(message)


def main(instructions: str) -> None:
    commands = read_instructions(instructions)
    asteroid = execute_commands(commands)
    messages = generate_messages(asteroid)
    print_messages(messages)


if __name__ == "__main__":
    instructions = sys.argv[1]
    main(instructions)
