import pycosat
from pprint import pprint

#returns variable number corresponding to a (cell, digit) choice
#range = 1..729

def var(i, j, digit):
	return 81 * (i - 1) + 9 * (j - 1) + (digit - 1) + 1

def generate_clauses():
	clauses = []

	for i in range(1, 10):
		for j in range(1, 10):

			#each cell must have a digit out of 1..9
			clauses.append([var(i,j,d) for d in range(1,10)])

			#these clauses are equivalent to the cell not taking more than one value out of 1..9
			#explanation can be found in the paper referenced
			for d1 in range(1,10):
				for d2 in range(d1 + 1,10):
					clauses.append([-var(i,j,d1), -	var(i,j,d2)])

	#print len(clauses)					
	
	#This ensures that each cell in the given set of cells has a distinct value out of 1..9
	#Since the number of cells is also 9, this also ensures all the digits are used
	def distinct(cells):
		_clauses = []
		for i in cells:
			for m in cells:
				for d in range(1,10):

					#This if condition prevents addition of redudant constraints which are symmetric w.r.t OR operator
					if var(i[0],i[1],d) < var(m[0],m[1],d):
						_clauses.append([-var(i[0],i[1],d), -var(m[0],m[1],d)])

		return _clauses


	for i in range(1,10):
		row_cells = []
		for j in range(1,10):

			#for each row, distinct should hold
			row_cells.append((i,j))
		
		clauses.extend(distinct(row_cells))
		

	for j in range(1,10):
		col_cells = []
		for i in range(1,10):
		
			#for each column, distinct should hold
			col_cells.append((i,j))
		
		clauses.extend(distinct(col_cells))
		

	for i in range(1,4):
		for j in range(1,4):
			three_cross_three_cells = []
			for a in range(3*i - 2, 3*i + 1):
				for b in range(3*j - 2, 3*j + 1):
		
					three_cross_three_cells.append((a,b))
			
			clauses.extend(distinct(three_cross_three_cells))
			

	return clauses

def solve(puzzle):
	clauses = generate_clauses() 
	#print clauses
	print "Total number of Clauses: ", len(clauses)


	#Add clauses corresponding to initial state of puzzle
	for i in range(1,10):
		for j in range(1,10):
			d = puzzle[i-1][j-1]

			if d != 0:
				clauses.append([var(i,j,d)])
	pycosat.solve(clauses)
	solution = set(pycosat.solve(clauses))

	
	final_solution = puzzle[:]

	for i in range(1,10):
		for j in range(1,10):
			for d in range(1,10):
				if var(i,j,d) in solution:
					final_solution[i-1][j-1] = d
	return final_solution
if __name__ == "__main__":

	hard = [[0, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 6, 0, 0, 0, 0, 3],
            [0, 7, 4, 0, 8, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 3, 0, 0, 2],
            [0, 8, 0, 0, 4, 0, 0, 1, 0],
            [6, 0, 0, 5, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 7, 8, 0],
            [5, 0, 0, 0, 0, 9, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 4, 0]]

	solution = solve(hard)
	
	

	pprint(solution)