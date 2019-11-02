import array

class ArrayList():

    def __init__(self):
        self.current_idx = 0
        self.array_list = array.array('i')

    def append(self, value):
        print(len(self.array_list))
        self.array_list[self.current_idx] = value
        self.current_idx += 1

def main():
    al = ArrayList()
    al.append(2)
    print(al.array_list)

if __name__ == '__main__':
    main()