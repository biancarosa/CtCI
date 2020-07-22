import timeit


class ArrayList():

    def __init__(self):
        self.current_index = 0
        self.array_list = [None, None]
        self.current_len = 2

    def append(self, value):
        if self.current_index >= self.current_len:
            self.array_list.extend([None] * self.current_len)
            self.current_len = self.current_len * 2
        self.array_list[self.current_index] = value
        self.current_index += 1


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
