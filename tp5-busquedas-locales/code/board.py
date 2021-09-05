from random import randint

class Board(ObjetiveBoard):

    def __init__(self, _size: int, _states: int):
        ObjetiveBoard.__init__(self, _size, _states)
        self.board = [randint(0, _size-1) for _ in range(_size)]
        self.table = [[30 for _ in range(_size)] for _ in range(_size)]
        self.__states = _states
        self.__fn_obj = self.update_fn()

    def update(self):


    def update_fn(self):

        def row(_: int) -> None:
            for __ in range(_+1, len(self.board)):
                if self.board[_] == self.board[__]:
                    self.__fn_obj += 1

        def diag_up(_: int) -> None:
            i: int = 1
            for __ in range(_+1, len(self.board)):
                if (self.board[_] - i) == self.board[__]:
                    self.__fn_obj += 1
                i += 1

        def diag_down(_: int) -> None:
            i: int = 1
            for __ in range(_+1, len(self.board)):
                if (self.board[_] + i) == self.board[__]:
                    self.__fn_obj += 1
                i += 1

        self.__fn_obj = 0
        for _ in range(len(self.board)):
            row(_)
            diag_up(_)
            diag_down(_)

    def get_states(self):
        return self.__states

    def update_states(self):
        self.__states = -1

