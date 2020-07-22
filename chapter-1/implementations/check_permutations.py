# Given two strings, write a method to define if one is a permutation of another

def is_permutation(a, b):
    if len(a) != len(b):
        return False
    a = sorted(a)
    b = sorted(b)
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True

def main():
    print(is_permutation('oi', 'io'))
    print(is_permutation('not a permutation', 'at all'))
    print(is_permutation('apermutation', 'arepumtitano'))

if __name__ == '__main__':
    main()