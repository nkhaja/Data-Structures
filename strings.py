#!python

import string


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing"""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)

def contains(text, sub):
    return contains_iterative(text,sub)


def is_palindrome_iterative(text):
    for i in range(0, len(text)/2):
        revIndex = (i+1)*(-1)
        if text[i] != text[revIndex]:
            return False
    return True





def is_palindrome_recursive(text, left=None, right=None):
    if len(text) < 2:
        return True

    left = 0 if left is None else left
    right = (len(text) - 1) if right is None else right

    if left >= right:
        return True

    if text[left] != text[right]:
        return False

    else:
        return is_palindrome_recursive(text, left = left + 1, right = right - 1)



def contains_iterative(string, sub):
    #insert condition for either being blank
    if string == "":
        return True

    success = ""
    for i in range(len(string)):
        if string[i] == sub[len(success)]:
            success = success + string[i]
        else:
            success = string[i]
        if success == sub:
            return True
    return False



def contains_recursive(string, sub, success='', carry=0):
    if len(sub) == 0 or sub==success:
        return True


    elif carry == len(string) or len(sub) > len(string):
        return False

    if string[carry] == sub[len(success)]:
        success = success + string[carry]
        return contains_recursive(string, sub, success, carry = carry + 1)

    else:
        success = string[carry]
        return contains_recursive(string, sub, success, carry = carry + 1)



def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            str_not = 'a' if is_pal else 'not a'
            print('{}: {} is {} palindrome'.format(result, repr(arg), str_not))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
    # print is_palindrome('radar')
    # print contains_iterative("hop", "chope")
    # print contains_iterative("snotty", "good")
    # print contains_iterative("a","a")
    # print contains_iterative("something", "thing")
    print contains_recursive("bobisgreatcheese", "great")
    print contains_recursive("a", "")
    print contains_recursive("","a")

    print contains_recursive("snotty", "good")
    print contains_recursive("something", "thing")
