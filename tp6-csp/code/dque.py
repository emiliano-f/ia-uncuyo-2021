from collections import deque

class Queue(deque):
    def __init__(self):
        deque.__init__(self)

    def is_empty(self):
        return False if len(self) > 0 else True
