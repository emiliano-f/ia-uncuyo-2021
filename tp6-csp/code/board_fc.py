class BoardFC:

    def __init__(self, _size: int):
        self.board = [Link(_size) for _ in range(_size)]

class Link:
    def __init__(self, _size):
        self.domain = [True for _ in range(_size)]
        self.counter = [0 for _ in range(_size)]
        self.length = _size

    def delete_domain_element(self, _queen, _row: int):
        _queen.domain[_row] = False
        _queen.counter[_row] += 1 # Queens threatening
        _queen.length -= 1
        #self.domain[_row] = False
        #self.counter[_row] += 1 # Queens threatening
        #self.length -= 1

    def restore_domain_element(self, _queen, _row: int):
        _queen.counter[_row] -= 1 # Queens threatening
        if _queen.counter[_row] == 0:
            _queen.domain[_row] = True
        _queen.length += 1
