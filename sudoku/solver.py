import math
import numpy as np
import sys 
import ipdb

def solve(grid: list):
	print("Start Solver:\n")
	solution = []
	grid = np.array(grid)

	ridx = 0
	cidx = 0
	position = (ridx, cidx)

	
	open_positions = np.where(grid==0)

	pointer = 0
	
	while pointer < len(open_positions[0]):
		position = open_positions[0][pointer],open_positions[1][pointer]

		if find_candidate(grid, position)[0]:
			candidate = find_candidate(grid, position)[1]
			grid[position] = candidate
			pointer += 1
		
		else:
			negative_pointer = pointer - 1

			while negative_pointer >=0:
			
				position = open_positions[0][negative_pointer],open_positions[1][negative_pointer]
				
				if find_increment(grid, position)[0]:
					candidate = find_increment(grid, position)[1]
					grid[position] = candidate
					pointer = negative_pointer + 1	
					break

				grid[position] = 0
				negative_pointer -= 1

				if (negative_pointer == -1):
					raise 

	print(f"Valid Solution:\n {grid}")
	return grid

def find_candidate(grid , position: tuple):
	for candidate in np.arange(1,10,1):
		if valid_candidate(candidate, grid, position):
			return (True , candidate)

	return (False, None)

def find_increment(grid, position):
	for candidate in np.arange(grid[position],10,1):
		if valid_candidate(candidate, grid, position):
			return (True, candidate)
	
	return (False, None)			


def valid_candidate(candidate: int, grid: list, position: tuple):
	"""Check that the candidate does not violate the freuqnecy condition
	in the corresponding row, column and box.

	Parameters
	----------
	candidate : int
	    Description
	grid : list
	    Description
	position : tuple
	    (row, col)
	"""

	row = grid[position[0],:]
	col = grid[:,position[1]]
	box = get_grid(grid, position)

	if (candidate in row) or (candidate in col) or (candidate in box):
		return False 
	
	return True
		


def get_grid(grid: list, position: tuple):
	"""Retrive the grid to the corresponding position.	
	The common grid is 9x9 and there are 3 boxes vertically and horizontally

	grid = ( 
		Box1 Box2 Box3
		Box4 Box5 Box6
		Box7 Box8 Box9	
	)

	"""

	grid = np.array(grid)

	box_h = position[0] // 3
	box_v = position[1]    // 3

	ridx_from = 3 * box_h
	ridx_to  = 3 * box_h + 3 
	cidx_from = 3 * box_v
	cidx_to = 3 * box_v + 3 

	return grid[ridx_from:ridx_to , cidx_from:cidx_to]

