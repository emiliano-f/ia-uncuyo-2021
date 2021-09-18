# This algorithm uses:
#
#
#
#
#

from random import random, randint

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

class Genetic:
    def __init__(self,
                 _size_board: int,
                 _pobl_size: int,
                 _parents_size: int,
                 _max_mutation: int):

        self.individuals = [Board(_size_board) for _ in range(_pobl_size)]
        self.size_board = _size_board
        self.size_poblat = _pobl_size
        self.size_parents = _parents_size
        self.max_mutation = _max_mutation
        self.mutation_probability = 0.10
        self.average = 0

    def __list_average__(self) -> None:
            summa: float = 0.0
            for _ in self.individuals:
                summa += _.get_fn()
            self.average = summa / len(self.individuals)

    def __check__(self, _boards: list[Board]) -> bool:
        for _ in range(len(_boards)):
            if _boards[_].get_fn() == 0:
                return True
        return False

    def __select_parents__(self) -> list[Board]:
        """ Proportional selection """

        idx: int = 0                # Index for self.individuals
        k: int = self.size_parents  # Index for parents selected
        probability: float = 0.35   # Probability of be selected
        select: list[Board] = []
        while k > 0:
            self.individuals[idx]
            if random() <= probability:
                select.append(self.individuals[idx])
                k -= 1
            idx = (idx + 1) % self.size_poblat
        return select

    def __crossover__(self, _parents: list[Board]) -> list[Board]:
        """ One point """

        descendants: list[Board] = [] # New children
        children: tuple[list, list] # Pair generated

        for _ in range(self.size_parents // 2):
            children = ([],[])
            fst: list = _parents[2*_].board
            snd: list = _parents[2*_+1].board
            for __ in range(self.size_board // 2):
                children[0].append(fst[__])
                children[1].append(snd[__])
            for __ in range(self.size_board // 2, self.size_board):
                children[1].append(fst[__])
                children[0].append(snd[__])

            descendants.append(Board(0,children[0]))
            descendants.append(Board(0,children[1]))

        return descendants

    def __replacement__(self, _descendants: list[Board]) -> None:
        """ Replacement of above-average performers """

        idx: int = 0 # Index for _descendants
        for _ in range(self.size_poblat):
            if self.individuals[_].get_fn() > self.average:
                self.individuals[_] = _descendants[idx]
                idx += 1
                if idx >= self.size_parents: # len(_descendants)
                    break
        self.__list_average__()

    def __mutation__(self) -> bool: # Temporal value
        """ If there is mutation, choose randomly """

        def mutate(_board: Board) -> None:
            """ Mutate elements on board: k elements """

            i: int                      # Index of mutation
            k: int = 2                  # elements to mutate
            top_idx: int = self.size_board - 1
            for _ in range(k):
                i = randint(0, top_idx)
                _board.board[i] = randint(0, top_idx)

        idx: int                # Index for individuals
        temp: list = []         # Check individuals
        max_idx: int = self.size_poblat - 1
        for _ in range(self.max_mutation):
            idx = randint(0, max_idx)
            mutate(self.individuals[idx])
            self.individuals[idx].update_fn()
            temp.append(self.individuals[idx])
        if self.__check__(temp):
            return True
        return False

    def think(self) -> tuple[bool, int]:

        ######## Part II
        prev_status: int = 20
        ################

        # Initialization -> Average and solution check
        self.__list_average__()
        if self.__check__(self.individuals):
            return (True, prev_status)

        for _ in range(1000):
            parents: list = self.__select_parents__()
            descendants: list = self.__crossover__(parents)
            prev_status += 10
            if self.__check__(descendants):
                return (True, prev_status)
            self.__replacement__(descendants)
            if random() <= self.mutation_probability:
                prev_status += 3
                value = self.__mutation__()
                if value:
                    return (True, prev_status)
            self.__list_average__()
        return (False, prev_status)

