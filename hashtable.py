class HashTable():
    LEN = 10
    def __init__(self):
        self.hash_table = [[] for _ in range(self.LEN)]

    def _get_hash(self, key):
        return hash(key) % self.LEN

    # TODO: Keys are equal
    def add(self, key, value):
        h = self._get_hash(key)
        self.hash_table[h].append((key, value))

    # TODO: Delete and get

def main():
    ht = HashTable()
    ht.add('one', 1)
    print(ht.hash_table)

if __name__ == '__main__':
    main()