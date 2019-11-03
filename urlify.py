# Given a string and its size, replace all spaces with %20

def urlify(string, length):
    lst = [None] * len(string)
    j = 0
    for i in range(length):
        if string[i] == ' ':
            lst[j] = '%'
            lst[j+1] = '2'
            lst[j+2] = '0'
            j += 3
        else:
            lst[j] = string[i]
            j += 1
    return ''.join(lst)

def main():
    print(urlify('Mr John Smith    ', 13))

if __name__ == '__main__':
    main()