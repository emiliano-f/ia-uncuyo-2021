class Heap:
    """ Min Binary Heap definition """
    def __init__(self, _length: int):
        self.heap = [-1 for _ in range(_length)]
        self.__index_last = -1

    def is_empty(self) -> bool:
        return self.__index_last < 0

    def insert(self, _value: int) -> int:

        self.heap[self.get_last_index() + 1] = _value
        self.__index_last += 1
        return self.__property_up()

    def get_min(self) -> int:

        if not self.is_empty():
            value: int = self.heap[0]
            self.heap[0] = self.heap[self.get_last_index()]
            self.delete_last_index()
            self.__property_down()
            return value
        return None

    def get_last_index(self) -> int:
        return self.__index_last

    def delete_last_index(self):
        if not self.is_empty():
            self.heap[self.get_last_index()] = -1
            self.__index_last -= 1

    def __shift_up(self, _: int):
        temp: int = self.heap[_]
        self.heap[_] = self.heap[_//2]
        self.heap[_//2] = temp

    def __is_child_minor(self, _: int):
        return self.heap[_//2] > self.heap[_]

    def __shift_down(self, _: int, _side: bool):
        temp: int = self.heap[_]
        if _side:
            self.heap[_] = self.__right_child(_)
            self.heap[_*2 + 2] = temp
        else:
            self.heap[_] = self.__left_child(_)
            self.heap[_*2 + 1] = temp

    def __property_up(self) -> int:

        _: int = self.get_last_index()
        while _ > 0:
            if self.__is_child_minor(_):
                self.__shift_up(_)
                _ = _//2
            else:
                break
        return _

    def __min_child(self, _: int) -> tuple:

        if _*2+2 < len(self.heap):
            if self.heap[_*2+2] != -1:
                minor: int = min(self.heap[_*2+1], self.heap[_*2+2])
                if self.heap[_*2+2] == minor:
                    return self.heap[_*2+2]
        return self.heap[_*2+1]

    def __property_down(self) -> int:

        _: int = 0
        while _*2+1 <= self.get_last_index():
            print(_, self.heap[_],end="")
            child: bool = self.__min_child(_)
            print(child, end="")
            if self.heap[_] < child:
                temp = _*2 + 1
                if self.heap[temp] == child:
                    self.__shift_down(_, False)
                    _ = temp
                else:
                    self.__shift_down(_, True)
                    _ = temp + 1
            else:
                break
        return _

    def __left_child(self, _idx: int) -> int:

        left: int = _idx*2+1
        if left < len(self.heap):
            return self.heap[left]
        return None

    def __right_child(self, _idx: int) -> int:

        right: int = _idx*2+2
        if right < len(self.heap):
            return self.heap[right]
        return None
