from Grid import Grid
from Game import Game
import numpy as np

# Input all parameters

# Grid dimensions
dims = input("Enter comma separated grid dimensions - width, height\n")
dims = dims.split(',')
width = int(dims[0])
height = int(dims[1])

# Intializing the grid
gen_zero = np.zeros((height, width))

# Row input
print("Enter Initial Grid")
for i in range(height):
    row = input()
    row = [ int(cell) for cell in row ]
    gen_zero[i] = row[:]

# Cell indices
cell_idx = input("Enter comma separated cell indices\n")
cell_idx = cell_idx.split(",")
x = int(cell_idx[0])
y = int(cell_idx[1])

# Total number of cycles
cycles = input("Enter number of runs\n")
cycles = int(cycles)
grid = Grid(gen_zero)

# Initialization and game execution
game = Game(grid, cycles, y, x)
game.play()
print("Green counter: " + str(game.result()))