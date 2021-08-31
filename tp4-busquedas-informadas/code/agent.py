from environment import Environment
from graph import Graph
from queue import PriorityQueue
from dque import Queue

class Agent:
    """ Agent definition """

    def __init__(self,
            _environ: Environment,
            _graph: Graph):

        self.environment = _environ
        self.graph = _graph.graph
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

    def heuristic(self, _pos: tuple) -> int:

        env: Environment = self.environment
        return round(((_pos[0]-env.destX)**2 + (_pos[1]-env.destY)**2)**0.5)

    def load_heuristic(self) -> None:
        env: Environment = self.environment
        for _ in range(env.size):
            for __ in range(env.size):
                if not env.floor[_][__]:
                    self.graph[env.get_state(_,__)].heuristic = self.heuristic((_,__))

    def think(self) -> None:

        def solved(_goal: int):
            node: int = _goal
            solution: Queue = Queue()
            while node != None:
                solution.appendleft(node)
                node = self.graph[node].parent
            return solution

        def init_relax():
            for _ in self.graph:
                _.visited = False

        def relax(_u: int, _v: int, _v_weigth: int):
            accum_v: int = self.graph[_v].accumulate
            accum_u: int = self.graph[_u].accumulate
            if accum_v == 0 or accum_v > (accum_u + _v_weigth):
                self.graph[_v].accumulate = accum_u + _v_weigth
                self.graph[_v].parent = _u

        env: Environment = self.environment
        state: int = env.get_state(env.initX, env.initY)
        goal: int = env.get_state(env.destX, env.destY)
        if state == goal:
            solution: Queue = Queue()
            solution.append(state)
            return solution

        #init_relax()
        frontier: PriorityQueue = PriorityQueue()
        frontier.put((0,state))
        ### ver si esto va aqui
        self.graph[state].accumulate = 0
        self.graph[state].accum_heur = self.graph[state].heuristic
        node: Node

        while not frontier.empty():
            state = frontier.get()
            state = state[1]
            print(state)
            self.states += 1
            self.graph[state].visited = True
            node = self.graph[state].head
            while node != None:
                vert = self.graph[node.value]
                #if not vert.visited:
                if vert.visited == None:
                    vert.parent = state
                    vert.accumulate = self.graph[state].accumulate + node.weigth
                    vert.accum_heur = vert.accumulate + vert.heuristic
                    if node.value == goal:
                        return solved(goal)
                    frontier.put((vert.accum_heur,node.value))
                    vert.visited = False
                node = node.next
