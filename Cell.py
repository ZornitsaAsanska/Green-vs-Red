from Color import Color

class Cell(object):

    def __init__(self, color):
        if color:
            self.color = Color.GREEN
        else:
            self.color = Color.RED

    def __str__(self):
        if self.color:
            return('1')
        else:
            return('0')