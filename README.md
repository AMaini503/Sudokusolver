# Sudokusolver
An implementation of an SAT based sudoku solver.

**Reference**: Weber, Tjark. "A SAT-based Sudoku solver." LPAR. 2005

**Introduction**

Sudoku is a number placement puzzle. The game consists of 9 X 9 grid i.e. 81 cells, each of which is to be filled with a digit out of set N = {1, 2, 3, 4, 5, 6, 7, 8, 9}. 

Following is an example of an unsolved sudoku puzzle 
![alt tag]()

The grid has a few cells filled and the player is expected to fill the remaining cells to reaach a valid solution. A valid solution must satisfy the following constraints :

 - Each row must contain all the digits from N
 - Each column must contain all the digits from N
 - Each column must contain all the digits from N


