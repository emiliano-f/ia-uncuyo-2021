from random import randint

class Board(ObjetiveBoard):

    def __init__(self, _size: int, _states: int):
        ObjetiveBoard.__init__(self, _size, _states)
        self.board = [randint(0, _size-1) for _ in range(_size)]
        self.table = [[30 for _ in range(_size)] for _ in range(_size)]
        self.__temp = [0 for _ in range(_size)]
        self.__states = _states
        self.__fn_obj = self.update_fn()

    def update(self):

        def row(_col: int, _row: int) -> None:
            for _ in range(len(self.board)):
                if _ != _col: # Different columns
                    if self.board[_] == _row:
                        temp += 1

        def diag_up(_col: int, _row: int) -> None:
            i: int = _row - 1
            _: int = _col + 1
            while i >= 0 and _ < len(self.board):
                if self.board[_] == i:
                    temp += 1
                i -= 1
                _ += 1

            i = _row + 1
            _ = _col - 1
            while i < len(self.board) and _ >= 0:
                if self.board[_] == i:
                    temp += 1
                i += 1
                _ -= 1

        def diag_down(_: int) -> None:
            i: int = _row - 1
            _: int = _col - 1
            while i >= 0 and _ >= 0 :
                if self.board[_] == i:
                    temp += 1
                i -= 1
                _ -= 1

            i = _row + 1
            _ = _col + 1
            while i < len(self.board) and _ < len(self.board):
                if self.board[_] == i:
                    temp += 1
                i += 1
                _ += 1

        temp: int
        for col in range(len(self.board)):
            temp = self.get_fn() - self.__temp[col]
            for rw in range(len(self.board)):
                if self.board[col] != rw: #False: update_fn
                    row(col, rw)
                    diag_up(col, rw)
                    diag_down(col, rw)
                    self.table[rw][col] = temp

    def update_fn(self):

        def row(_: int) -> None:
            for __ in range(_+1, len(self.board)):
                if self.board[_] == self.board[__]:
                    self.__fn_obj += 1
                    self.__temp[_] += 1
                    self.__temp[__] += 1

        def diag_up(_: int) -> None:
            i: int = 1
            for __ in range(_+1, len(self.board)):
                if self.board[_] - i < 0: # Out of range
                    continue
                if (self.board[_] - i) == self.board[__]:
                    self.__fn_obj += 1
                    self.__temp[_] += 1
                    self.__temp[__] += 1
                i += 1

        def diag_down(_: int) -> None:
            i: int = 1
            for __ in range(_+1, len(self.board)):
                if self.board[_] + i >= len(self.board): # OoR
                    continue
                if (self.board[_] + i) == self.board[__]:
                    self.__fn_obj += 1
                    self.__temp[_] += 1
                    self.__temp[__] += 1
                i += 1

        self.__fn_obj = 0
        for _ in range(len(self.board)):
            self.__temp[_] = 0
        for _ in range(len(self.board)):
            row(_)
            diag_up(_)
            diag_down(_)

        for _ in range(len(self.board)):
            self.table[self.board[_]][_] = self.get_fn()

    def get_states(self):
        return self.__states

    def update_states(self):
        self.__states = -1

    def get_fn(self) -> int:
        return self.__fn_obj

