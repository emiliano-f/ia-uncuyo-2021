from board import Board
import csv

class HillClimbingStd(Board):

    def __init__(self, _size: int, _states: int):
        Board.__init__(self, _size)
        self.states = _states

    def get_states(self) -> int:
        return self.__states

    def update_states(self) -> None:
        self.__states = -1

    def think(self) -> list:

        def update_min() -> None:
            for r in range(len(self.table)):
                for c in range (len(minimum[0])):
                    if self.board[c] != r: # Extract min from neighbors in col
                        if minimum[1][c] >= self.table[r][c]:
                            minimum[0][c] = r
                            minimum[1][c] = self.table[r][c]

        def extract_min(_last: int) -> tuple:
            row: int
            fn: int
            pos: int
            if _last != 0:
                row = minimum[0][0]
                fn = minimum[1][0]
                pos = 0
            else:
                row = minimum[0][1]
                fn = minimum[1][1]
                pos = 1

            for _ in range(1, len(minimum[0])):
                if _last != _ and fn > minimum[1][_]:
                    row = minimum[0][_]
                    fn = minimum[1][_]
                    pos = _
            return (pos, row, fn)

        self.update_fn()
        self.update()
        minimum = [[_ for _ in self.board], # [Rows]
                    [self.get_fn() for _ in self.board]] # [Obj Fn]
        last: int = None
        new: int

        ## Part II
        prv_stts: list = [] # Previous states
        prv_stts.append(self.get_fn())
        success: bool = False
        ##

        while self.states > 0:
            update_min()
            new = extract_min(last)
            #if new[2] > self.get_fn(): # Never happens
            #    break
            self.board[new[0]] = new[1]
            self.update_fn()
            self.update()
            self.states -= 1
            last = new[0]
            if new[2] == 0:
                success = True
                break

            prv_stts.append(self.get_fn())

        return (success,prv_stts)
