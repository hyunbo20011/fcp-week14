#Grids 1-4 are 2x2
grid1 = [
		[1, 1, 1, 1],
		[1, 1, 1, 1],
		[1, 1, 1, 1],
		[1, 1, 1, 1]]

grid2 = [
		[1, 0, 4, 2],
		[4, 2, 1, 3],
		[0, 1, 0, 4],
		[3, 4, 2, 1]]

grid3 = [
		[1, 2, 3, 4],
		[2, 1, 4, 3],
		[3, 4, 2, 1],
		[4, 3, 1, 2]]

grid4 = [
		[1, 3, 4, 2],
		[4, 2, 1, 3],
		[2, 1, 3, 4],
		[3, 4, 2, 1]]

#Grids 4-7 are 3x3
grid5 = [
		[1, 2, 3, 4, 5, 6, 7, 8, 9,],
		[2, 3, 4, 5, 6, 7, 8, 9, 1,],
		[3, 4, 5, 6, 7, 8, 9, 1, 2,],
		[4, 5, 6, 7, 8, 9, 1, 2, 3,],
		[5, 6, 7, 8, 9, 1, 2, 3, 4,],
		[6, 7, 8, 9, 1, 2, 3, 4, 5,],
		[7, 8, 9, 1, 2, 3, 4, 5, 6,],
		[8, 9, 1, 2, 3, 4, 5, 6, 7,],
		[9, 1, 2, 3, 4, 5, 6, 7, 8,]]

grid6 = [
		[6, 1, 7, 8, 4, 2, 5, 3, 9,],
		[7, 4, 5, 3, 6, 9, 1, 8, 2,],
		[8, 3, 2, 1, 7, 5, 4, 6, 9,],
		[1, 5, 8, 6, 9, 7, 3, 2, 4,],
		[9, 6, 4, 2, 3, 1, 8, 7, 5,],
		[2, 7, 3, 5, 8, 4, 6, 9, 1,],
		[4, 8, 7, 9, 5, 6, 2, 1, 3,],
		[3, 9, 1, 4, 2, 8, 7, 5, 6,],
		[5, 2, 6, 7, 1, 3, 9, 4, 8,]]

grid7 = [
		[6, 1, 9, 8, 4, 2, 5, 3, 7,],
		[7, 4, 5, 3, 6, 9, 1, 8, 2,],
		[8, 3, 2, 1, 7, 5, 4, 6, 9,],
		[1, 5, 8, 6, 9, 7, 3, 2, 4,],
		[9, 6, 4, 2, 3, 1, 8, 7, 5,],
		[2, 7, 3, 5, 8, 4, 6, 9, 1,],
		[4, 8, 7, 9, 5, 6, 2, 1, 3,],
		[3, 9, 1, 4, 2, 8, 7, 5, 6,],
		[5, 2, 6, 7, 1, 3, 9, 4, 8,]]

#grids 8-10 are 2x3
grid8 = [
		[0, 0, 6, 0, 0, 3],
		[5, 0, 0, 0, 0, 0],
		[0, 1, 3, 4, 0, 0],
		[0, 0, 0, 0, 0, 6],
		[0, 0, 1, 0, 0, 0],
		[0, 5, 0, 0, 6, 4]]

grid9 = [
		[1, 2, 6, 5, 4, 3],
		[5, 3, 4, 6, 2, 1],
		[6, 1, 3, 4, 5, 2],
		[2, 5, 5, 3, 1, 6],
		[4, 6, 1, 2, 3, 5],
		[3, 5, 2, 1, 6, 4]]

grid10 = [
		[1, 2, 6, 5, 4, 3],
		[5, 3, 4, 6, 2, 1],
		[6, 1, 3, 4, 5, 2],
		[2, 4, 5, 3, 1, 6],
		[4, 6, 1, 2, 3, 5],
		[3, 5, 2, 1, 6, 4]]


grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), 
		(grid5, 3, 3), (grid6, 3, 3), (grid7, 3, 3),
		(grid8, 2, 3), (grid9, 2, 3), (grid10, 2, 3)]

expected_outputs = [False, False, False, True, False, False, True, False, False, True]

'''
===================================
DO NOT CHANGE CODE ABOVE THIS LINE
===================================
'''
def check_section(section, n):
	if len(set(section)) == len(section) and sum(section) == sum([i for i in range (n+1)]):
		return True
	return False

def get_squares(grid, n_rows, n_cols):
	squares = []
	for i in range (n_cols):
		rows = (i*n_rows, (i+1)*n_rows)
		for j in range(n_rows):
			cols = (j*n_cols, (j+1)*n_cols)
			square = []
			for k in range(rows[0], rows[1]):
				line = grid[k][cols[0]:cols[1]]
				square += line
			squares.append(square)

	return(squares)

#To complete the first assignment, please write the code for the following function
def check_solution(grid_input):
	'''
	This function is used to check whether a sudoku board has been correctly solved

	args: grid - representation of a suduko board as a nested list.
	returns: True (correct solution) or False (incorrect solution)
	'''

	grid = grid_input[0]
	n_rows = grid_input[1]
	n_cols = grid_input[2]
	n = n_rows*n_cols

	for row in grid:
		if check_section(row,n) == False:
			return False
		
	for i in range(n_rows):
		column = []
		for row in grid:
			column.append(row[i])
		if check_section(column, n) == False:
			return False
		
	squares = get_squares(grid, n_rows, n_cols)
	for sqaure in sqaures:
		if check_section(sqaure, n)  == False:
			return False
		
	return None




'''
===================================
DO NOT CHANGE CODE BELOW THIS LINE
===================================
'''
def main():
	'''
	This function will call the check_solution function on each of the provided grids, 
	comparing the answer to the expected output. Each correct output is given 10 'points
	'''

	points = 0

	print("Running test script for coursework 1")
	print("====================================")
	
	#Loop through the grids and expected outputs together
	for (i, (grid, output)) in enumerate(zip(grids, expected_outputs)):

		#Compare output to expected output
		print("Checking grid: %d" % (i+1))
		checker_output = check_solution(grid)

		if checker_output == expected_outputs[i]:
			#Output is correct - yay!
			print("grid %d correct" % (i+1))
			points = points + 5
		else:
			#Output is incorrect - print both output and expected output.
			print("grid %d incorrect" % (i+1))
			print("Output was: %s, but expected: %s" % (checker_output, expected_outputs[i]))

	print("====================================")
	print("Test script complete, Total points: %d" % points)


if __name__ == "__main__":
	main()