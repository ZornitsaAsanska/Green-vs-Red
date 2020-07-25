from Color import Color

class Cell(object):

    def __init__(self, color):
        if color == 1:
            self.color = Color.GREEN
        else:
            self.color = Color.RED

    def __str__(self):
        '''
        Overwriting str to improve grid readability
        '''
        if self.color == Color.GREEN:
            return('1')
        else:
            return('0')