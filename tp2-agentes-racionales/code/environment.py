import random

class Environment:
    """ Environment definition """

    def __init__(self,
            _sizeX: int, _sizeY: int,
            _posX: int, _posY: int,
            _dirt_rate: float):

        def create() -> list:
            """ Initialization of floor: clean """
            floor: list = []
            row: list = []
            for _ in range(_sizeX):
                for __ in range(_sizeY):
                    row.append(False)
                floor.append(row)
                row.clear()
            return floor

        def to_dirty(_floor: list):
            """ Random dirt """
            tiles: int = round(_sizeX*_sizeY*_dirt_rate)
            count: int = 0
            x: int = 0
            y: int = 0
            randX: int = _sizeX-1
            randY: int = _sizeY-1

            while count < tiles:
                x = random.randint(0,randX)
                y = random.randint(0,randY)
                if not _floor[x][y]:
                    _floor[x][y] = True
                    count += 1
            return _floor

        self.floor = to_dirty(create())
        self.initial_rate = _dirt_rate
        self.dirt_rate = _dirt_rate
        self.sizeX = _sizeX
        self.sizeY = _sizeY
        self.posX = _posX
        self.posY = _posY
        self.dirt_tiles = round(_sizeX*_sizeY*dirt_rate)

    def is_dirty(self) -> tuple:

        if self.dirt_tiles == 0:
            return (False, self.dirt_rate, self.dirt_tiles)
        return (True, self.dirt_rate, self.dirt_tiles)

    def get_position(self) -> tuple:

        return (self.posX, self.posY)

    def get_performance(self):

    def print_environment(self) -> None:

        for _ in range(self.sizeX):
            print("[", end='')
            for __ in range(self.sizeY):
                if self.floor[_][__]:
                    print("D|", end='')
                else:
                    print(" |", end='')
            print("]")
