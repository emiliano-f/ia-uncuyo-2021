from environment import Environment

class Agent:
    """ Agent definition """

    def __init__(self,
            _environ : Environment, _actions: int = 1000):
        self.environment = _environ
        self.actions = _actions

    def up(self) -> None:

        if self.environment.posY > 0: #if the table is 1x1?
            if self.has_actions():
                self.environment.posY -= 1
                self.actions -= 1

    def down(self) -> None:

        if self.environment.posY < self.environment.sizeY - 1:
            if self.has_actions():
                self.environment.posY += 1
                self.actions -= 1

    def left(self) -> None:

        if self.environment.posX > 0:
            if self.has_actions():
                self.environment.posX -= 1
                self.actions -= 1

    def right(self) -> None:

        if self.environment.posX < self.environment.sizeX - 1:
            if self.has_actions():
                self.environment.posX += 1
                self.actions -= 1

    def to_up(self) -> None:
        """ Moves to up before acting """

        while self.environment.posY > 0:
            self.up()
            self.act()
            if not self.has_actions():
                break

    def to_down(self) -> None:
        """ Moves to down before acting """

        while self.environment.posY < self.environment.sizeY-1:
            self.down()
            self.act()
            if not self.has_actions():
                break

    def to_right(self) -> None:
        """ Moves to the right before acting """

        while self.environment.posX < self.environment.sizeX-1:
            self.right()
            self.act()
            if not self.has_actions():
                break

    def to_left(self) -> None:
        """ Moves to the left before acting """

        while self.environment.posX > 0:
            self.left()
            self.act()
            if not self.has_actions():
                break

    def suck(self) -> None:

        env: Environment = self.environment
        if self.has_actions():
            self.environment.floor[env.posY][env.posX] = False
            self.actions -= 1

    def idle(self) -> None:
        """ Zzz... """

        if self.has_actions():
            self.actions -= 1

    def perspective(self, _environ: Environment = None) -> bool:

        env: Environment = self.environment
        return self.environment.floor[env.posY][env.posX]

    def act(self) -> None:

        if self.perspective:
            self.suck()
        else:
            self.idle()

    def get_actions(self) -> int:

        return self.actions

    def has_actions(self) -> bool:

        if self.actions > 0:
            return True
        return False
