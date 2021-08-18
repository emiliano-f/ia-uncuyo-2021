from environment import Environment

class Agent:
    """ Agent definition """
    def __init__(self,
            _environ : Environment):
        self.environment = _environ

    def up(self) -> None:

        if self.environment.posY < self.environment.sizeY - 1:
            self.environment.posY += 1

    def down(self) -> None:

        if self.environment.posY > 0: #if the table is 1x1?
            self.environment.posY -= 1

    def left(self) -> None:

        if self.environment.posX > 0:
            self.environment.posX -= 1

    def right(self) -> None:

        if self.environment.posX < self.environment.sizeX - 1:
            self.environment.posX += 1

    def to_up(self) -> None:
        """ Moves to up before acting """

        while env.posY < self.environment.sizeY-1:
            self.up()
            self.act()

    def to_down(self) -> None:
        """ Moves to down before acting """

        while self.environment.posY > 0 :
            self.down()
            self.act()

    def to_right(self) -> None:
        """ Moves to the right before acting """

        while self.environment.posX < self.environment.sizeX-1:
            self.right()
            self.act()

    def to_left(self) -> None:
        """ Moves to the left before acting """

        while self.environment.posX > 0:
            self.left()
            self.act()

    def suck(self) -> None:

        env: Environment = self.environment
        self.environment.floor[env.posX][env.posY] = False

    def idle(self) -> None:
        """ Zzz... """
        return None

    def perspective(self, _environ: Environment = None) -> bool:

        env: Environment = self.environment
        return self.environment.floor[env.posX][env.posY]

    def act(self) -> None:

        if self.perspective:
            self.suck()
        else:
            self.idle()
