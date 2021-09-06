from random import randint

class Board:

    def __init__(self, _size: int):
        self.board = [randint(0, _size-1) for _ in range(_size)]
        self.table = [[30 for _ in range(_size)] for _ in range(_size)]
        self.__temp = [0 for _ in range(_size)]
        self.__fn_obj = self.update_fn() # Not working!

    def update(self):

        def row(_col: int, _row: int) -> int:
            tmp: int = 0
            for c in range(len(self.board)):
                if c != _col: # Different columns
                    if self.board[c] == _row:
                        tmp += 1
            return tmp

        def diag_up(_col: int, _row: int) -> int:
            tmp: int = 0
            r: int = _row - 1
            c: int = _col + 1
            while r >= 0 and c < len(self.board):
                if self.board[c] == r:
                    tmp += 1
                r -= 1
                c += 1

            r = _row + 1
            c = _col - 1
            while r < len(self.board) and c >= 0:
                if self.board[c] == r:
                    tmp += 1
                r += 1
                c -= 1
            return tmp

        def diag_down(_col: int, _row: int) -> int:
            tmp: int = 0
            r: int = _row - 1
            c: int = _col - 1
            while r >= 0 and c >= 0 :
                if self.board[c] == r:
                    tmp += 1
                r -= 1
                c -= 1

            r = _row + 1
            c = _col + 1
            while r < len(self.board) and c < len(self.board):
                if self.board[c] == r:
                    tmp += 1
                r += 1
                c += 1
            return tmp

        temp: int
        for col in range(len(self.board)):
            for rw in range(len(self.board)):
                temp = self.get_fn() - self.__temp[col]
                if self.board[col] != rw: #False: update_fn
                    temp += row(col, rw)
                    temp += diag_up(col, rw)
                    temp += diag_down(col, rw)
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
        return self.get_fn()

    def get_fn(self) -> int:
        return self.__fn_obj

    def print_table(self) -> None:
        for _ in self.table:
            print(_)
