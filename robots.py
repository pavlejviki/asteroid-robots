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
    pass


def main(instructions: str) -> None:
    commands = read_instructions(instructions)



if __name__ == "__main__":
    instructions = sys.argv[1]
    main(instructions)
