from environment import Environment
from graph import Graph

class Agent:
    """ Agent definition """

    def __init__(self,
            _environ: Environment
            _graph: Graph):

        self.environment = _environ
        self.graph = _graph.graph

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

    def heuristic(self, _pos) -> int:

        env: Environment = self.environment
        return round(((_pos[0]-env.initX)**2 + (_pos[1]-env.initY)**2)**0.5)

    def load_heuristic(self) -> None:

        for _ in range(self.environment.size):
            for __ in range(self.environment.size):
                if not self.environment.floor[_][__]:
                    self.graph[self.environment.get_state(_,__)].heuristic = self.heuristic((_,__))

    def think(self) -> None:

