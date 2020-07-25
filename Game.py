from Grid import Grid
from Color import Color

class Game(object):

    def __init__(self, grid, cycles, x, y):
        self.grid = grid
        self.cycles = cycles
        self.x = x # row
        self.y = y # column
        self.current_cycle = 0
        # Green counter for cell (y,x)
        self.green_score = 0

    def play(self):
        '''
        Executes all cycles
        Updates the grid and green counter for specified cell (y,x) after each cycle
        '''
        while self.current_cycle < self.cycles:
            if self.grid.grid[self.x][self.y].color == Color.GREEN:
                self.green_score +=1
            self.grid.next()
            #    Debugging
            # print(self.grid)
            # print("-"*self.grid.width)
            self.current_cycle +=1
        if self.grid.grid[self.x][self.y].color == Color.GREEN:
            self.green_score +=1

    def result(self):
        '''
        Returns final result - green score for specified cell
        '''

        if self.current_cycle == self.cycles:
            return(self.green_score)
        else:
            raise Exception("Final Cycle has not been reached")

    def __str__(self):
        '''
        Overwrites str method
        Returns the grid at current cycle
        '''
        output = "Current cycle: " + str(self.current_cycle) + "/n"
        output += str(self.grid)
        return output