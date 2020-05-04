"""Sudoku solver"""
import numpy as np

class SudokuSolver():

    def __init__(self):
        pass

    def __call__(self, grid: list) -> list:
        """Solve the given sudoku grid using backtracking (brute force).

        See: https://en.wikipedia.org/wiki/Sudoku_solving_algorithms

        Parameters
        ----------
        grid : list
            Sudoku grid with blanks

        Returns
        -------
        grid : list
            Solved sudoku grid
        """

        grid = np.array(grid)
        print(f"\nStart Solving:\n {grid}\n")

        open_positions = np.where(grid == 0)

        candidate_pointer = 0
        while candidate_pointer < len(open_positions[0]):

            position = get_position(candidate_pointer, open_positions)
            candidate = find_candidate(grid, position)

            if isinstance(candidate, int):
                grid[position] = candidate
                candidate_pointer += 1
            else:

                update_pointer = candidate_pointer - 1

                while update_pointer >= 0:

                    position = get_position(update_pointer, open_positions)
                    update = find_increment(grid, position)

                    if isinstance(update, int):
                        grid[position] = update
                        candidate_pointer = update_pointer + 1
                        break

                    grid[position] = 0
                    update_pointer -= 1

                    if update_pointer == -1:
                        raise

        print(f"Valid Solution:\n {grid}")
        return grid


def get_position(pointer: int, open_positions: list) -> tuple:
    """Return the current position indizes (row,col)

    Parameters
    ----------
    pointer : int
        Points to the current open position
    open_positions : list
        List of all open positions that need to be filled with a
        number between 1 and 9

    Returns
    -------
    tuple
        The current position (row,col)
    """
    return open_positions[0][pointer], open_positions[1][pointer]


def find_candidate(grid: list, position: tuple) -> int:
    """Retrieve a possible candidate for the given position

    Parameters
    ----------
    grid : list
        Sudoku Grid
    position : tuple
        Current position on grid (row,col)

    Returns
    -------
    int
        A possible candidate
    """
    for candidate in np.arange(1, 10, 1):
        if valid_candidate(candidate, grid, position):
            return int(candidate)
    return None


def find_increment(grid: list, position: tuple) -> int:
    """Retrieve the first possible increment for the given position

    Parameters
    ----------
    grid : list
        Sudoku Grid
    position : tuple
        Current position on grid (row,col)

    Returns
    -------
    int
        A possible increment
    """
    for update in np.arange(grid[position]+1, 10, 1):
        if valid_candidate(update, grid, position):
            return int(update)

    return None


def valid_candidate(candidate: int, grid: list, position: tuple):
    """Check that the candidate does not violate the frequency condition
    in the corresponding row, column and box.

    Parameters
    ----------
    candidate : int
        Description
    grid : list
        Sudoku Grid
    position : tuple
        Current position on grid (row,col)

    Returns
    -------
    boolean
        Indicator whether candidate violates the frequency condition or
        not.
    """

    row = grid[position[0], :]
    col = grid[:, position[1]]
    box = get_box(grid, position).flatten()
    
    present_values = set(np.concatenate((row,col,box),axis=0))
    
    return not (candidate in present_values)


def get_box(grid: list, position: tuple):
    """Retrive the grid to the corresponding position.
    The common grid is 9x9 and there are 3 boxes vertically and horizontally

    grid = (
        Box1 Box2 Box3
        Box4 Box5 Box6
        Box7 Box8 Box9
    )

    Parameters
    ----------
    grid : list
        Sudoku Grid
    position : tuple
        Current position on grid (row,col)

    Returns
    -------
    list
        The corresponding box of the current position on the grid

    """

    box_h = position[0] // 3
    box_v = position[1] // 3

    ridx_from = 3 * box_h
    ridx_to = 3 * box_h + 3
    cidx_from = 3 * box_v
    cidx_to = 3 * box_v + 3

    return grid[ridx_from:ridx_to, cidx_from:cidx_to]
