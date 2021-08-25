from agent import Agent
from environment import Environment
from dque import Queue
from graph import Graph, Node

class BreadthSearchAgent(Agent):

    def __init__(self,
                 _environ: Environment,
                 _graph: Graph):

        Agent.__init__(self, _environ)
        self.graph = _graph

    def think(self) -> None:

        def solved(_goal: int):
            node: int = _goal
            solution: Queue = Queue()
            while node != None:
                solution.appendleft(node)
                node = self.graph[node].parent
            return solution

        env: Environment = self.environment
        state: int = env.get_state(env.initX, env.initY)
        goal: int = env.get_state(env.destX, env.destY)
        if state == goal:
            solution: Queue = Queue()
            solution.append(state)
            return solution

        frontier: Queue = Queue()
        explored: Queue = Queue()
        frontier.appendleft(state)
        adj: int
        node: Node

        while not frontier.is_empty():
            state = frontier.pop()
            node = self.graph[state].head
            while node != None:
                if self.graph[node.value].visited == None:
                    frontier.appendleft(node.value)
                    self.graph[node.value].visited = False
                    self.graph[node.value].parent = state
                    if node.value == goal:
                        return solved(goal)
                node = node.next
            self.graph[state].visited = True

