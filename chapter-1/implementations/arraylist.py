import timeit


class ArrayList():

    def __init__(self):
        self.index = 0
        self.array_list = [None, None]
        self.capacity = 2

    def append(self, value):
        if self.index >= self.capacity:
            self.array_list.extend([None] * self.capacity)
            self.capacity = self.capacity * 2
        self.array_list[self.index] = value
        self.index += 1


def main():
    start = timeit.default_timer()
    al = ArrayList()
    for i in range(5):
        al.append(i)
    stop = timeit.default_timer()
    print('Time: ', stop - start)
    start = timeit.default_timer()
    al = []
    for i in range(5):
        al.append(i)
    stop = timeit.default_timer()
    print('Time: ', stop - start)


if __name__ == '__main__':
    main()
