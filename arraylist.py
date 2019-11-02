import array

class ArrayList():

    def __init__(self):
        self.current_idx = 0
        self.array_list = array.array('i', 2 )

    def append(self, value):
        print(len(self.array_list))
        # how the fuck do i double this size? should i really be doing this?
        self.array_list[self.current_idx] = value
        self.current_idx += 1

def main():
    al = ArrayList()
    al.append(2)
    print(al.array_list)

if __name__ == '__main__':
    main()