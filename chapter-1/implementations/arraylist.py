import timeit
import ctypes


class ArrayList:

    def __init__(self, capacity=2):
        self.index = 0
        self.capacity = capacity
        self.array_list = [None for _ in range(self.capacity)]

    def append(self, value):
        if self.index >= self.capacity:
            self._resize()
        self.array_list[self.index] = value
        self.index += 1

    def _resize(self):
        self.array_list.extend([None] * self.capacity)
        self.capacity = self.capacity * 2


class ArrayListV2:

    def __init__(self, capacity=2):
        self.index = 0
        self.capacity = capacity
        self.array_list = [None for _ in range(self.capacity)]

    def append(self, value):
        if self.index >= self.capacity:
            self._resize()
        self.array_list[self.index] = value
        self.index += 1

    def _resize(self):
        self.capacity = self.capacity * 2
        new_array_list = [None for _ in range(self.capacity)]
        for i in range(self.index):
            new_array_list[i] = self.array_list[i]
        self.array_list = new_array_list


class ArrayListV3:

    def __init__(self, capacity=2):
        self.index = 0
        self.capacity = capacity
        self.array_list = (self.capacity * ctypes.c_int64)()

    def append(self, value):
        if self.index >= self.capacity:
            self._resize()
        self.array_list[self.index] = value
        self.index += 1

    def _resize(self):
        self.capacity = self.capacity * 2
        new_array_list = (self.capacity * ctypes.c_int64)()
        for i in range(self.index):
            new_array_list[i] = self.array_list[i]
        self.array_list = new_array_list


def main():
    n = 100000

    start = timeit.default_timer()
    al = []
    for i in range(n):
        al.append(i)
    stop = timeit.default_timer()
    print('Time: ', stop - start)

    start = timeit.default_timer()
    al = ArrayList(n)
    for i in range(n):
        al.append(i)
    stop = timeit.default_timer()
    print('Time V1: ', stop - start)

    start = timeit.default_timer()
    al = ArrayListV2(n)
    for i in range(n):
        al.append(i)
    stop = timeit.default_timer()
    print('Time V2: ', stop - start)

    start = timeit.default_timer()
    al = ArrayListV3(n)
    for i in range(n):
        al.append(i)
    stop = timeit.default_timer()
    print('Time V3: ', stop - start)


if __name__ == '__main__':
    main()
