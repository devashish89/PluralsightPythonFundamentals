
def is_palindrome(input):
    l1 = list(str(input))
    l2 = list(reversed(list(str(input))))
    print(l1, l2)
    if l1==l2:
        return True
    else:
        return False



if __name__ == "__main__":
    print(is_palindrome(12321))
    print(is_palindrome("02022020"))
    print(is_palindrome(123))

