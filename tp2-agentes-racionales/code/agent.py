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
        #actua tomando una perspectiva, y decide si limpiar o no
        #como es una accion, aqui deberiamos disminuir del 1000
        if self.perspective:
            self.suck()
        else:
            self.idle()

    def think(self):

        def nearest() -> tuple:

            env: Environment = self.environment
            row: bool
            col: bool
            if env.sizeX - (env.posX +1) <= env.sizeX // 2:
                row = True # to right
            else:
                row = False # to left

            if env.sizeY - (env.posY +1) <= env.sizeY // 2:
                col = True # to up
            else:
                col = False # to down

            return (row,col)

        def to_corner():

            dest: tuple = nearest()

            if dest[0]:
                self.act()
                self.to_right()
            else:
                self.act()
                self.to_left()

            if dest[1]:
                self.to_up()
            else:
                self.to_down()

        def sweep():

            corner: tuple = self.environment.get_position()
            env: Environment = self.environment
            flag_to_right: bool
            if corner[0] == 0:
                flag_to_right = True
            else:
                flag_to_right = False

            for _ in range(env.sizeY):
                if flag_to_right:
                    self.to_right()
                else:
                    self.to_left()

                if corner[1] == 0: #(0,0)
                    self.up()
                else: #(0,sizeY-1)
                    self.down()

                if _ < env.sizeY-1:
                    self.act()

                flag_to_right = not(flag_to_right)

        to_corner()
        sweep()
