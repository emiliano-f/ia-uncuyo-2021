from environment import Environment

class Agent:
    """ Agent definition """

    def __init__(self,
            _environ : Environment):
        self.environment = _environ
        self.states = 0

    def up(self) -> None:

        if self.environment.posY > 0: #if the table is 1x1?
            self.environment.posY -= 1

    def down(self) -> None:

        if self.environment.posY < self.environment.sizeY - 1:
            self.environment.posY += 1

    def left(self) -> None:

        if self.environment.posX > 0:
            self.environment.posX -= 1

    def right(self) -> None:

        if self.environment.posX < self.environment.sizeX - 1:
            self.environment.posX += 1

    def perspective(self, _environ: Environment = None) -> bool:

        env: Environment = self.environment
        return self.environment.floor[env.posY][env.posX]
