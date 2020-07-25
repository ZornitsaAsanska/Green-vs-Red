from Grid import Grid
from Game import Game
import numpy as np

# Grid dimensions
dims = input("Enter comma separated grid dimensions - width, height\n")
dims = dims.split(',')
width = int(dims[0])
height = int(dims[1])

# Intializing the grid
gen_zero = np.zeros((height, width))

# Row input
for i in range(height):
    row = input()
    row = [ int(cell) for cell in row ]
    gen_zero[i] = row[:]

# Cell indices
cell_idx = input("Enter comma separated cell indices\n")
cell_idx = cell_idx.split(",")
x = int(cell_idx[0])
y = int(cell_idx[1])

# Total numeber of cycles
cycles = input("Enter number of runs\n")
cycles = int(cycles)
print(gen_zero)
grid = Grid(gen_zero)
print(grid)
print(grid.grid[1][1].color)
game = Game(grid, cycles, y, x)
game.play()
print(game.result())





