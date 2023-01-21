import json
import sys

from typing import Generator


from robot import (
    Robot,
    CommandType,
    Bearing,
    Movement,
)
from asteroid import Asteroid


def read_instructions(instructions: str) -> Generator[str, None, None]:
    """
    Reads a file of instructions in JSON format, and returns a list of commands.
    Each command is represented as a dictionary.
    """

    with open(instructions, "r") as file:
        for row in file:
            command = json.loads(row)
            yield command


def execute_commands(commands) -> Asteroid:
    """
    Executes a list of commands on an asteroid and returns the final state of the asteroid.
    """
    new_asteroid = None
    new_robot = None
    for command in commands:
        if CommandType(command["type"]) == CommandType.NEW_ASTEROID:
            new_asteroid = Asteroid(command["size"]["x"], command["size"]["y"])
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
    """
    Generates messages describing the final positions of the robots on an asteroid, in the form of JSON strings.
    """
    for robot in asteroid.robots:
        robot_details = {
            "type": "robot",
            "position": {"x": robot.x, "y": robot.y},
            "bearing": robot.bearing.value,
        }
        yield json.dumps(robot_details)


def print_messages(messages: Generator[str, None, None]) -> None:
    """
    Prints all messages from a generator of messages.
    """
    for message in messages:
        print(message)


def main(instructions: str) -> None:
    """
    The main function that runs the program, it takes the name of the file with instructions as input
    and  follows this process:
    1. parse the instructions into a list of commands using read_instructions() function.
    2. execute the commands on an asteroid using execute_commands() function.
    3. generate messages about the current state of robots on the asteroid using generate_messages() function.
    4. print the generated messages using print_messages() function.
    """

    commands = read_instructions(instructions)
    asteroid = execute_commands(commands)
    messages = generate_messages(asteroid)
    print_messages(messages)


if __name__ == "__main__":
    instructions = sys.argv[1]
    main(instructions)
