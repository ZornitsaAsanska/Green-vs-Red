from Grid import Grid
from Color import Color

class Game(object):

    def __init__(self, grid, cycles, x, y):
        self.grid = grid
        self.cycles = cycles
        self.x = x
        self.y = y
        self.current_cycle = 0
        self.green_score = 0

    def play(self):
        if not self.current_cycle == self.cycles:
            while self.current_cycle < self.cycles:
                if self.grid[self.x][self.y] == Color.GREEN:
                    self.green_score +=1
                self.grid.next()
                self.current_cycle +=1

    def result(self):
        if self.current_cycle == self.cycles:
            return(self.green_score)
        else:
            raise Exception("Final Cycle has not been reached")

    def __str__(self):
        output = "Current cycle: " + str(self.current_cycle) + "/n"
        output += str(self.grid)
        return output