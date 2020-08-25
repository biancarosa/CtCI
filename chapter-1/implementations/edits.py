# Given a str write a method to define if they're one or zero characters away
def one_away(a, b):
    diff = len(a) - len(b)
    if abs(diff) > 1:
        return False
    count = 0
    if len(a) > len(b):
        bigger_str = a
        smaller_str = b
    else:
        bigger_str = b
        smaller_str = a
    j = 0
    i = 0
    while i < len(smaller_str):
        if smaller_str[i] == bigger_str[j]:
            i += 1
        else:
            if diff == 0:
                i += 1
            count += 1
        j += 1
        if count > 1:
            return False
    return True


def main():
    print(one_away('pale', 'ple'))
    print(one_away('pales', 'pale'))
    print(one_away('pale', 'bale'))
    print(one_away('pale', 'bake'))
    print(one_away('ple', 'pale'))
    print(one_away('pale', 'pales'))
    print(one_away('bale', 'pale'))
    print(one_away('bake', 'pale'))


if __name__ == '__main__':
    main()
