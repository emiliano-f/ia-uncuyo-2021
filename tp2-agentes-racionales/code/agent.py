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

        env: Environment = self.environment
        self.environment.floor[env.posX][env.posY] = False

    def idle(self):

        print("Zzz")

    def perspective(self, _environ):

        env: Environment = self.environment
        return self.environment.floor[env.posX][env.posY]

    def think(self):

        def to_corner():

            def nearest() -> Tuple:

                env: Environment = self.environment
                if env.sizeX - (env.posX +1) <= env.sizeX // 2:
                    row = True # to right
                else:
                    row = False # to left

                if env.sizeY - (env.posY +1) <= env.sizeY // 2:
                    col = True # to up
                else:
                    col = False # to down

                return (row,col)

