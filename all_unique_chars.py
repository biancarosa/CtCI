# Suppose you have to find all unique chars in a string and you can't use any data structures.
from hashtable import HashTable

def main():
    string = 'string bem grande pra gente ver os caracteres unicos'
    ht = HashTable()
    for char in string:
        count = ht.get(char)
        if count == None:
            count = 1
        else:
            count += 1
        ht.add(char, count)
    print('Unique chars are :: ')
    [print(item[0]) if item[1] == 1 else None for sublist in ht.hash_table for item in sublist]

if __name__ == '__main__':
    main()