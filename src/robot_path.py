"""
Date: 02.Oct.2024
Author: Harish Natarajan Ravi
Email: harrish.nr@gmail.com
"""


"""
robot_path:
    Calculates the robot's trajectory based on a sequence of moves.

    Args:
        moves: A string of characters representing the robot's moves.
               Valid characters are '>' (right), '<' (left), '^' (up), and 'v' (down).

    Returns:
        A boolean indicating whether the path is closed - Square and Rectangle or not.
"""

def robot_path(moves):
    # Handle the case of no input
    if moves == None:
        return False
    
    # Initialize counters for each direction
    down = 0
    up = 0
    left = 0
    right = 0

    for c in moves:
        if c == 'v':
            down += 1
        elif c == '<':
            left += 1
        elif c == '>':
            right += 1
        elif c == '^':
            up += 1
        else:
            break
    
    flag = False
    # Check if the path is closed (equal number of up/down and left/right moves)
    if (up == down) and (right == left):
        if up == right:
            path = "square"
            
        elif (up > right) or (right > up):
            path = "rectangle"
        print("Path is: ", path)
        flag = True
    else:
        path = "Incomplete Path"
        flag = False

    return flag

"""
verify_code:
    Prints a message based on the path completion status.

    Args:
        flag: A boolean indicating whether the path is closed or not.
"""
def verify_code(flag):
    if flag == True:
        print("Closed path")
    elif flag == False:
        print("Incomplete path or No valid moves")

if __name__ == "__main__":
    moves = input("Enter the robot's moves: ")
    path_taken = robot_path(moves)
    verify_code(path_taken)


    
    