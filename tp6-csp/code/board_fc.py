class BoardFC:

    def __init__(self, _size: int):
        self.board = [Link(_size) for _ in range(_size)]

class Link:
    def __init__(self, _size):
        self.domain = [True for _ in range(_size)]
        self.counter = [0 for _ in range(_size)]
        self.length = _size

    def delete_domain_element(self, _row: int):
        if self.domain[_row]:
            self.length -= 1
        self.domain[_row] = False
        self.counter[_row] += 1 # Queens threatening

    def restore_domain_element(self, _row: int):
        self.counter[_row] -= 1 # Queens threatening
        if self.counter[_row] == 0:
            self.domain[_row] = True
            self.length += 1
