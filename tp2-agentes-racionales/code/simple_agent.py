from agent import Agent
from environment import Environment

class SimpleAgent(Agent):

    def __init__(self, _environ: Environment):

        Agent.__init__(self, _environ):

    def think(self) -> None:

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

        def to_corner() -> None:

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

        def sweep() -> None:

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
