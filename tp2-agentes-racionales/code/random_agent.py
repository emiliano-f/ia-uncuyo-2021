from agent import Agent
from environment import Environment
import random

class RandomAgent(Agent):

    def __init__(self, _environ: Environment):

        Agent.__init__(self, _environ)

    def think(self) -> None:

        while self.has_actions():
            self.act()
            to = random.randint(0,3)
            if to == 0:
                self.up()
            elif to == 1:
                self.down()
            elif to == 2:
                self.right()
            else:
                self.left()
