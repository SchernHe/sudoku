# Sudoku Solver

## Backtracking

A brute force algorithm that iterates over all open blanks and fills the positions with numbers of 1-9, given that one of these numbers does not violate on of the following constraints:
* Each number is only allowed to occur once in each row
* Each number is only allowed to occur once in each column
* Each number is only allowed to occur once in each box

In case there is no possible candidate for the current position, go one step back and increase the latest position by one. Again only if the increment does not violate aforementioned constraints.
See: [Backtracking Wikipedia](https://en.wikipedia.org/wiki/Sudoku_solving_algorithms)

