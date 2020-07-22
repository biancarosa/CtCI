import array
from ctypes import c_int


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
    al = ArrayList()
    al.append(1)
    print(al.array_list)
    al.append(2)
    print(al.array_list)
    al.append(3)
    print(al.array_list)
    al.append(4)
    print(al.array_list)
    al.append(5)
    print(al.array_list)


if __name__ == '__main__':
    main()
