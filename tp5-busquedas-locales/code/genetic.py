# This algorithm uses:
#
#
#
#
#

from random import random, randint

class Genetic:
    def __init__(self,
                 _size_board: int,
                 _pobl_size: int,
                 _parents_size: int,
                 _max_mutation: int):

        self.individuals = [Board(_size_board) for _ in range(_pobl_size)]
        self.size_board = _size_board
        self.size_parents = _parents_size
        self.max_mutation = _max_mutation
        self.mutation_probability = 0.10
        self.average = 0.0

    def __list_average__(self) -> None:
            summa: float = 0.0
            for _ in self.individuals:
                summa += _.get_fn()
            self.average = summa / len(self.individuals)

    def __check__(self, _boards: list) -> bool:
        for _ in range(len(_boards)):
            if _boards[_].get_fn() == 0:
                return True
        return False

    def think(self) -> bool:

        def select_parents() -> list:
            """ Proportional selection """

            k: int = 10
            idx: int = 0
            length: int = len(self.individuals)
            probability: float = 0.35
            select: list = []
            while k > 0:
                self.individuals[idx]
                if random() < probability:
                    select.append(self.individuals[idx])
                    k -= 1
                idx = (idx + 1) % length
            return select

        def crossover(_parents: list) -> list:
            """ Three points """

            def update_descendants() -> None:
                for _ in range(self.size_parents):
                    descendants[_].update_fn()

            # Points: 1, 3, 5
            descendants: list[Board] = []
            children: tuple[list, list]
            i: int
            for _ in range(len(_parents) // 2):
                children = ([],[])
                fst: list = _parents[2*_]
                snd: list = _parents[2*_+1]
                i = 0
                for __ in range(self.size_board):
                    children[i%2].append(fst.board[__])
                    children[(i+1)%2].append(snd.board[__])
                    if __ % 2:
                        i += 1
                descendants.append(Board(0,children[0]))
                descendants.append(Board(0,children[1]))

            update_descendants()
            return descendants

        def replacement(_descendants: list) -> None:
            """ Replacement of below-average performers """

            idx: int = 0
            for _ in range(len(self.individuals)):
                if self.individuals[_].get_fn() < self.average:
                    self.individuals[_] = _descendants[idx]
                    idx += 1
                    if idx >= len(_descendants):
                        break
            self.__list_average__()

        def mutation() -> bool: # Temporal value
            """ If there is mutation, choose randomly """

            def mutate(_board: Board) -> None:
                """  """

                i: int
                k: int = 2
                top_idx: int = self.size_board - 1
                for _ in range(k):
                    i = randint(0, top_idx)
                    _board.board[i] = randint(0, top_idx)

            idx: int
            temp: list = []
            max_idx: int = len(self.individuals) - 1
            for _ in range(self.max_mutation):
                idx = randint(0, max_idx)
                mutate(self.individuals[idx])
                self.individuals[idx].update_fn()
                temp.append(self.individuals[idx])
            if self.__check__(temp):
                return True
            return False

        # Initialization -> Average and solution check
        self.__list_average__()
        if self.__check__(self.individuals):
            return True

        for _ in range(1000):
            parents: list = select_parents()
            descendants: list = crossover(parents)
            if self.__check__(descendants):
                return True
            replacement(descendants)
            if random() <= self.mutation_probability:
                value = mutation()
                if value:
                    return True
            self.__list_average__()
        return False

class Board:

    def __init__(self,
                 _size: int,
                 _board: list = None):
        if _board == None:
            self.board = [randint(0, _size-1) for _ in range(_size)]
        else:
            self.board = _board
        self.__fn_obj = self.update_fn() # Not working!

    def update_fn(self) -> int:

        def row(_: int) -> None:
            for __ in range(_+1, len(self.board)):
                if self.board[_] == self.board[__]:
                    self.__fn_obj += 1

        def diag_up(_: int) -> None:
            i: int = 1
            for __ in range(_+1, len(self.board)):
                if self.board[_] - i < 0: # Out of range
                    continue
                if (self.board[_] - i) == self.board[__]:
                    self.__fn_obj += 1
                i += 1

        def diag_down(_: int) -> None:
            i: int = 1
            for __ in range(_+1, len(self.board)):
                if self.board[_] + i >= len(self.board): # OoR
                    continue
                if (self.board[_] + i) == self.board[__]:
                    self.__fn_obj += 1
                i += 1

        self.__fn_obj = 0
        for _ in range(len(self.board)):
            row(_)
            diag_up(_)
            diag_down(_)

        return self.get_fn()

    def get_fn(self) -> int:
        return self.__fn_obj
