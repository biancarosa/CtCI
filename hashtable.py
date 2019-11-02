# TODO: Delete
class HashTable():
    LEN = 10
    def __init__(self, length = LEN):
        self.length = length
        self.hash_table = [[] for _ in range(self.length)]

    def _get_hash(self, key):
        return hash(key) % self.length

    def add(self, key, value):
        h = self._get_hash(key)
        for i in range(len(self.hash_table[h])):
            if self.hash_table[h][i][0] == key:
                self.hash_table[h][i] = (key, value)
                return
        self.hash_table[h].append((key, value))

    def get(self, key):
        h = self._get_hash(key)
        for i in self.hash_table[h]:
            if i[0] == key:
                return i[1]
        return None

    def __str__(self):
        return str([i for i in self.hash_table])

def main():
    ht = HashTable()
    ht.add('one', 1)
    print(ht.hash_table)

if __name__ == '__main__':
    main()