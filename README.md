## Show Me The Robots!

A program that executes a series of JSON commands provided in a text file and outputs a series of JSON messages,  describing the final positions of the robots after all the input commands have been executed.

### How to run

To run this program, you will need to have Python and Git installed on your machine.

1. Clone the repository from GitLab by running the following command in your command prompt:
```
git clone https://gitlab.com/bct-interviews/viktoria-pavlej/asteroid-robots.git
```
2. Change into the project directory by running:
```
cd asteroid-robots
```
3. Create a virtual environment:
```
python -m venv venv
```
4. Activate the virtual environment:
```
source venv/bin/activate  # on macOS
venv\Scripts\activate  # on Windows 
```
5. Install the required dependencies:
```
pip install -r requirements.txt
```
6. Add an instructions.txt file in the project's main directory with the required instructions to be executed:
```
cat > instructions.txt
{"type": "asteroid", "size": {"x": 5, "y": 5}}
{"type": "new-robot", "position": {"x": 1, "y": 2}, "bearing": "north"}
{"type": "move", "movement": "turn-left"}
{"type": "move", "movement": "move-forward"}
{"type": "move", "movement": "turn-left"}
{"type": "move", "movement": "move-forward"}
{"type": "move", "movement": "turn-left"}
{"type": "move", "movement": "move-forward"}
{"type": "move", "movement": "turn-left"}
{"type": "move", "movement": "move-forward"}
{"type": "move", "movement": "move-forward"}
{"type": "new-robot", "position": {"x": 3, "y": 3}, "bearing": "east"}
{"type": "move", "movement": "move-forward"}
{"type": "move", "movement": "move-forward"}
{"type": "move", "movement": "turn-right"}
{"type": "move", "movement": "move-forward"}
{"type": "move", "movement": "move-forward"}
{"type": "move", "movement": "turn-right"}
{"type": "move", "movement": "move-forward"}
{"type": "move", "movement": "turn-right"}
{"type": "move", "movement": "turn-right"}
{"type": "move", "movement": "move-forward"}
ctrl + C
```

7. Run the program by:
```
python robots.py instructions.txt
```

The program will read the instructions from the provided file and execute them, then output the final state of the robots in json format to the console.
### Output

```
{"type": "robot", "position": {"x": 0, "y": 2}, "bearing": "west"}
{"type": "robot", "position": {"x": 5, "y": 3}, "bearing": "east"}
```

Note: Make sure the instruction file is in the correct format and contains valid json data, otherwise the program may raise errors.

### Tests

To run tests use:

```
python -m pytest tests/
```
