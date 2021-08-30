from agent import Agent
from environment import Environment
from dque import Queue
from graph import Graph, Node

class DepthLimitedSearchAgent(Agent):

    def __init__(self,
                 _environ: Environment,
                 _graph: Graph):

        Agent.__init__(self, _environ)
        self.graph = _graph.graph

    def think(self) -> Queue:

        env: Environment = self.environment
        state: int = env.get_state(env.initX, env.initY)
        goal: int = env.get_state(env.destX, env.destY)
        if state == goal:
            solution: Queue = Queue()
            solution.append(state)
            return solution

        return self.__rec_think(state, goal, 0, 45)


    def __rec_think(self, _node: int, _goal: int, _i: int, _limit: int) -> Queue:

        if _i < _limit:
            node: Node = self.graph[_node].head
            self.graph[_node].visited = False
            self.states += 1
            while node != None:
                if self.graph[node.value].visited == None:
                    self.graph[node.value].parent = _node
                    if node.value == _goal:
                        return self.__solved(_goal)
                    term: Queue = self.__rec_think(node.value, _goal, _i+1, _limit)
                    if term != None:
                        return term
                node = node.next
            self.graph[_node].visited = True

    def __solved(self, _goal: int) -> Queue:
        node: int = _goal
        solution: Queue = Queue()
        while node != None:
            solution.appendleft(node)
            node = self.graph[node].parent
        return solution
