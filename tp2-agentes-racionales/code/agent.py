from environment import Environment

class Agent:
    """ Agent definition """
    def __init__(self,
            _environ : Environment):
        self.environment = _environ

    def up(self):

        if self.environment.posY < self.environment.sizeY - 1:
            self.environment.posY += 1

    def down(self):

        if self.environment.posY > 0: #if the table is 1x1?
            self.environment.posY -= 1

    def left(self):

        if self.environment.posX > 0:
            self.environment.posX -= 1

    def right(self):

        if self.environment.posX < self.environment.sizeX - 1:
            self.environment.posX += 1

    def suck(self):

    def idle(self):

    def perspective(self, _environ):

    def think(self):
