from environment import Environment

class Graph:

    def __init__(self, _v: int):
        self.graph = [Link() for _ in range(_v)]


    def add(self, _v1: int, _v2: int):
        """ Add nodes, double adjacency """

        self.graph[_v1].head = Node(_v2, self.graph[_v1].head)
        self.graph[_v1].length += 1
        #self.graph[_v2].head = Node(_v1, self.graph[_v2].head)
        #self.graph[_v2].length += 1

    def show(self) -> None:
        """ Print graph """

        for _ in range(len(self.graph)):
            print("V:",_, "; length:", self.graph[_].length, "\n[",end="")
            node: Node = self.graph[_].head
            for __ in range(self.graph[_].length):
                print(node.value, end=",")
                node = node.next
            print("]")

    def load_environment(self, _env: Environment) -> None:
        """ Load environment to graph """

        def perspective(_row: int, _col: int) -> tuple:
            """ Returns perspective: (up, down, left, right) """

            return (True if _row == 0 else _env.floor[_row-1][_col],
                    True if _row == _env.size-1 else _env.floor[_row+1][_col],
                    True if _col == 0 else _env.floor[_row][_col-1],
                    True if _col == _env.size-1 else _env.floor[_row][_col+1])

        def adjacent(_row: int, _col: int) -> None:

            lim: tuple = perspective(_row, _col)
            v: int = _env.get_state(_row, _col)
            if not lim[0]:
                self.add(v, _env.get_state(_row-1,_col))
            if not lim[1]:
                self.add(v, _env.get_state(_row+1,_col))
            if not lim[2]:
                self.add(v, _env.get_state(_row, _col-1))
            if not lim[3]:
                self.add(v, _env.get_state(_row, _col+1))

        for _ in range(_env.size):
            for __ in range(_env.size):
                if not _env.floor[_][__]:
                    adjacent(_,__)

class Link:
    def __init__(self):
        self.head = None
        self.length = 0
        self.visited = None
        self.parent = None

class Node:
    def __init__(self,
                 _value: int = None,
                 _next = None):
        self.value = _value
        self.next = _next
