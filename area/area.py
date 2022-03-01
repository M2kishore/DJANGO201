from curses.ascii import isdigit


def calculate_square_area(side):
    """
    Calculates the area of a square, given a side
    """
    if isinstance(side, str):
        if isdigit(side):
            side = int(side)
        else:
            return -1
    return side * side
