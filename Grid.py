from Cell import Cell
from Color import Color

class Grid(object):

    def __init__(self, gen_zero):
        self.grid = [[] for row in gen_zero]
        for i, row in enumerate(gen_zero):
            self.grid[i] = [Cell(cell) for cell in row]
        self.height = len(gen_zero)
        self.width = len(gen_zero[0])
    
    def next(self):
        next_grid = [ [0]*self.width for i in range(self.height) ]
        for i in range(self.height):
            for j in range(self.width):
                green_neighbours = 0
                for x in range(max(0, i-1), min(i+1, self.height-1) + 1):
                    for y in range(max(0, j-1), min(j+1, self.height-1) + 1):
                        if (x != i or y != j) and self.grid[x][y].color == Color.GREEN:
                            green_neighbours +=1
                
                if self.grid[i][j].color == Color.RED:
                    if green_neighbours in [3,6]:
                        next_grid[i][j] = Cell(1)
                    else:
                        next_grid[i][j] = Cell(0)
                else:
                    if green_neighbours in [2,3,6]:
                        next_grid[i][j] = Cell(1)
                    else:
                        next_grid[i][j] = Cell(0)
        self.grid = next_grid

    def __str__(self):
        output = ""
        for row in self.grid:
            str_row = ""
            for cell in row:
                str_row += str(cell)
            str_row += '\n'
            output += str_row
        output = output[:-1]
        return output