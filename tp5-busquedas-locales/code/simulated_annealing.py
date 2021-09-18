import random
from board import Board
from math import pow
from math import e as euler

class SimulatedAnnealing(Board):

    def __init__(self, _size: int):
        Board.__init__(self, _size)

    def think(self):

        def random_neighbor() -> int:
            return random.randint(0, len(self.board) - 1)

        def get_random() -> float:
            return random.random()

        def probability(_diff: float, _x: int) -> float:

            def schedule() -> float:
                return 28/_x

            return pow(euler, _diff/schedule())

        def update_min() -> None:
            for r in range(len(self.table)):
                for c in range (len(minimum[0])):
                    if self.board[c] != r: # Extract min from neighbors in col
                        if minimum[1][c] >= self.table[r][c]:
                            minimum[0][c] = r
                            minimum[1][c] = self.table[r][c]

        def extract_min() -> tuple:

            row: int = minimum[0][0]
            fn: int= minimum[1][0]
            pos: int = 0

            for _ in range(1, len(minimum[0])):
                if fn > minimum[1][_]:
                    row = minimum[0][_]
                    fn = minimum[1][_]
                    pos = _
            return (pos, row, fn)

        def accept() -> None:
            update_min()
            new = extract_min()
            self.board[new[0]] = new[1]
            self.update_fn()
            self.update()

        neighbor: int
        iterat: int = 0
        self.update_fn()
        self.update()
        minimum = [[_ for _ in self.board], # [Rows]
                    [self.get_fn() for _ in self.board]] # [Obj Fn]

        dif1: int = self.get_fn()
        dif2: int = 0
        diff: int

        # Part II
        part_status: list = []
        part_status.append(self.get_fn())

        while self.get_fn() > 0 and iterat < 100: #Determining limit

            iterat += 1
            neighbor = random_neighbor()
            diff = dif1 - dif2

            if neighbor >= self.get_fn() or get_random() < probability(diff, iterat):
                accept()
                dif2 = dif1
                dif1 = self.get_fn()
            part_status.append(self.get_fn())

        return (self.get_fn() == 0, part_status)
