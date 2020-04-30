from sudoku.solver import get_box


def test_get_box():

    grid = [
        [7, 2, 6, 4, 9, 3, 8, 1, 5],
        [3, 1, 5, 7, 2, 8, 9, 4, 6],
        [4, 8, 9, 6, 5, 1, 2, 3, 7],
        [8, 5, 2, 1, 4, 7, 6, 9, 3],
        [6, 7, 3, 9, 8, 5, 1, 2, 4],
        [9, 4, 1, 3, 6, 2, 7, 5, 8],
        [1, 9, 4, 8, 3, 6, 5, 7, 2],
        [5, 6, 7, 2, 1, 4, 3, 8, 9],
        [2, 3, 8, 5, 7, 9, 4, 6, 1],
    ]

    expected_result = [
        [7, 2, 6],
        [3, 1, 5],
        [4, 8, 9],
    ]

    assert (expected_result == get_box(grid, (0, 0))).all()
    assert (expected_result == get_box(grid, (0, 1))).all()
    assert (expected_result == get_box(grid, (2, 0))).all()

    expected_result = [
        [8, 3, 6],
        [2, 1, 4],
        [5, 7, 9],
    ]

    assert (expected_result == get_box(grid, (8, 4))).all()

    expected_result = [
        [5, 7, 2],
        [3, 8, 9],
        [4, 6, 1],
    ]

    assert (expected_result == get_box(grid, (8, 8))).all()
