from board import Board

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
                for c in range (len(minimum)):
                    if self.board[c] != r:
                        if minimum[1][c] > self.table[r][c]:
                            minimum[0][c] = r
                            minimum[1][c] = self.table[r][c]

        def extract_min() -> tuple:
            ret: int = minimum[0][0]
            fn: int = minimum[1][0]
            pos: int = 0
            for _ in range(1, len(minimum[0])):
                if fn > minimum[1][_]:
                    ret = minimum[0][_]
                    fn = minimum[1][_]
                    pos = _
            return (pos, ret, fn)

        self.update_fn()
        self.update()
        minimum = [[self.board[_] for _ in self.board], # [Rows]
                    [self.get_fn() for _ in self.board]] # [Obj Fn]
        new: int
        while self.states > 0:
            update_min()
            new = extract_min()
            if new[2] > self.get_fn():
                break
            self.board[new[0]] = new[1]
            self.update_fn()
            self.update()
            self.states -= 1
        return self.board
