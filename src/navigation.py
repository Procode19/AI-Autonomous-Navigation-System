# Navigation module for controlling the robot movement

def get_next_move(path):
    """
    Returns the next position from the path.
    Modifies the path by removing the first element.
    """
    if path:
        return path.pop(0)
    return None