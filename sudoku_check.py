import numpy as np

def check_sudoku(grid):
    """ Return True if grid is a valid Sudoku square, otherwise False. """

    for i in range(9):
        # j, k index the top left-hand corner of each 3x3 tile
        j, k = (i // 3) * 3, (i % 3) * 3
        if len(set(grid[i,:])) != 9 or len(set(grid[:,i])) != 9 or len(set(grid[j:j+3, k:k+3].ravel())) != 9:
            return False
        return True

sudoku = """145327698
            839654127
            672918543
            496185372
            218473956
            753296481
            367542819
            984761211
            521839764"""

# Turn the provided string, sudoku, into an integer array
grid = np.array([[int(i) for i in line] for line in sudoku.split()])
print(grid)
if check_sudoku(grid):
    print('grid valid')
else:
    print('grid invalid')
