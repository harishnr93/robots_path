## Robots Path

This Python script helps you analyze a sequence of moves and determine if the robot's path forms a closed shape (square or rectangle).

**Features:**

- **Input Validation:** Checks for valid move characters (`^`, `v`, `<`, `>`).
- **Closed Path Detection:** Identifies if the robot returns to its starting position.
- **Shape Determination:** Distinguishes between square and rectangle paths.

**Getting Started**

1. **Prerequisites:** Python 3.x is required to run this script.

2. **Running the Script:**
   - Save this code as a Python file (e.g., `robot_path_checker.py`).
   - Open your terminal or command prompt and navigate to the directory where you saved the file.
   - Execute the script using the following command:

     ```bash
     python robot_path_checker.py
     ```

3. **Input Moves:**
   - The script will prompt you to enter a sequence of moves representing the robot's path.
   - Use the following characters to represent each direction:

     - `^`: Up
     - `v`: Down
     - `<`: Left
     - `>`: Right

4. **Output:**
   - Based on the provided moves, the script will display one of the following messages:

     - **Closed path:** If the path forms a square or rectangle.
     - **Incomplete path or No valid moves:** If the path is not closed or invalid moves are entered.

**Example Usage:**

```
Enter the robot's moves: ^^^<<<vvv>>>
Path is: square
Closed path
```

**Code Structure:**

- The script defines two functions:
    - `robot_path(moves)`:  This function analyzes the move sequence and determines if the path is closed. It calculates the direction counts and checks for balance between up/down and left/right movements. Additionally, it identifies the path shape (square or rectangle) for closed paths.
    - `verify_code(flag)`: This function interprets the boolean flag returned by `robot_path` and prints the corresponding message indicating the path completion status.

**Additional Notes:**

- The script assumes the robot starts at the origin (0, 0) and moves by one unit in each direction.
- Invalid characters or incomplete paths will result in the "Incomplete path or No valid moves" message.

**Feel free to modify or extend this script to suit your specific needs!**
