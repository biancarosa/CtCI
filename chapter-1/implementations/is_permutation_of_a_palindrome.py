# Given a string write a method to define if it's a permutation of a palindrome
def is_permutation_of_a_palindrome(str):
    sorted_str = sorted(str)
    count = {}
    for a in sorted_str:
        if a == ' ':
            continue
        count[a] = count.get(a, 0) + 1
    odd = 0
    even = 0
    for a in sorted_str:
        if a == ' ':
            continue
        if count[a] != 1 or count[a] % 2 == 0:
            even += 1
        else:
            odd += 1
        if odd > 1:
            return False
    return True


def main():
    print(is_permutation_of_a_palindrome('tact coat'))


if __name__ == '__main__':
    main()
