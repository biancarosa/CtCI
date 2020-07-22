import timeit


class StringBuilder():

    def __init__(self):
        self.strings = []

    def append(self, value):
        self.strings.append(value)

    def to_string(self):
        return ''.join(self.strings)


def main():
    words = ["polly", " ", "wants", " ", "a", " ", "cracker"] * 10000
    start = timeit.default_timer()
    sb = StringBuilder()
    for w in words:
        sb.append(w)
    sb.to_string()
    stop = timeit.default_timer()
    print('Time: ', stop - start)

    start = timeit.default_timer()
    s = ''
    for w in words:
        s += w
    s
    stop = timeit.default_timer()
    print('Time: ', stop - start)


if __name__ == '__main__':
    main()
