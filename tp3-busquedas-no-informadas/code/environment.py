import random

class Environment:
    """ Environment definition """

    def __init__(self,
            _initX: int, _initY: int,
            _destX: int, _destY: int,
            _obst_rate: float,
            _size: int = 100):

        def create() -> list:
            """ Initialization of floor: unobstructed """
            floor: list = []
            row: list = []
            for _ in range(_size):
                for __ in range(_size):
                    row.append(False)
                floor.append(row)
                row = []
            return floor

        def obstacles(_floor: list) -> list:
            """ Random obstacles """
            tiles: int = round(_size**2*_obst_rate)
            count: int = 0
            x: int = 0
            y: int = 0
            rand: int = _size-1

            while count < tiles:
                x = random.randint(0,rand)
                y = random.randint(0,rand)
                if not _floor[y][x]:
                    _floor[y][x] = True
                    count += 1
            return _floor

        if _initX < _size and _initY < _size:
            self.floor = obstacles(create())
            self.initial_rate = _obst_rate
            self.dirt_rate = _obst_rate
            self.size = _size
            self.initX = _initX
            self.initY = _initY
            self.posX = _initX
            self.posY = _initY
            self.destX = _destX
            self.destY = _destY
            self.obst_tiles = round(_size**2*_obst_rate)
            self.floor[_initX][_initY] = False
            self.floor[_destX][_destY] = False
        else:
            self.__del__()

    def __del__(self):

        return None

    def get_position(self) -> tuple:

        return (self.posX, self.posY)

    def get_tile_number(self, _row: int, _col: int) -> int:

        return _row*(self.size)+_col

    def print_environment(self) -> None:

        for _ in range(self.size):
            print("[", end='')
            for __ in range(self.size):
                if self.floor[_][__]:
                    print("X|", end='')
                else:
                    print(" |", end='')
            print("]")
