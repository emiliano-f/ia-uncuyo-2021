from agent import Agent
from environment import Environment
from dque import Queue
from graph import Graph, Node
from minheap import Heap
from queue import PriorityQueue

class UniformSearchAgent(Agent):

    def __init__(self,
                 _environ: Environment,
                 _graph: Graph):

        Agent.__init__(self, _environ)
        self.graph = _graph.graph

    def think(self) -> Queue:

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

        init_relax()
        frontier: PriorityQueue = PriorityQueue()
        frontier.put((0,state))
        node: Node

        while not frontier.empty():
            state = frontier.get()
            state = state[1]
            self.graph[state].visited = True
            node = self.graph[state].head
            while node != None:
                if not self.graph[node.value].visited:
                    frontier.put((node.weigth, node.value))
                    relax(state, node.value, node.weigth)
                node = node.next
        return solved(goal)
