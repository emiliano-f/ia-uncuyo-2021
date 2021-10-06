class BoardCSP:

    def __init__(self, _size: int):
        self.board = [_size for _ in range(_size)]
        self.domain = [_ for _ in range(_size)]
        self.constraints = [True for _ in range(_size)] #Alldiff(rows)
