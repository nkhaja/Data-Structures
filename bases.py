#!python

import string
import math

# def mapLetters():
#     alphabet = {}
#     alpha = "abcdefghijklmnopqrstuvwxyz"
#     for a, index in alpha.enumerate():
#         alphabet[a] = index + 10
#     return alphabet



def decode(str_num, base):
    """
    Decode given number from given base to base 10.
    str_num -- string representation of number in given base
    base -- base of given number
    """
    assert 2 <= base <= 36

    tally = 0
    digits = len(str_num)
    power = digits - 1
    for i in range(digits):
        num = None
        digit = str_num[i]
        if digit.isdigit():
            num = int(digit)
        else:
            num = ord(digit) - 97 + 10
        tally = tally + (base**power)*num
        power = power - 1
    return tally


def encode(num, base):
    """
    Encode given number from base 10 to given base.
    num -- the number in base 10
    base -- base to convert to
    """
    assert 2 <= base <= 36

    remainder = None
    output = []
    nextNum = num
    while nextNum is not 0:
        remainder = nextNum % base
        if remainder > 9:
            output.append(str((chr(remainder + 87))))
            nextNum = nextNum/base
        else:
            output.append(str(remainder))
            nextNum = nextNum/base

    output = output[::-1]
    return "".join(output)




def convert(str_num, base1, base2):
    """
    Convert given number from base1 to base2.
    """


    assert 2 <= base1 <= 36
    assert 2 <= base2 <= 36

    base_ten = decode(str_num, base1)
    targ_base = encode(base_ten, base2)

    return targ_base

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        str_num = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        result = convert(str_num, base1, base2)
        print('{} in base {} is {} in base {}'.format(str_num, base1, result, base2))
    else:
        print('Usage: {} number base1 base2'.format(sys.argv[0]))


if __name__ == '__main__':
    # main()
    print decode('101',2)
    print encode(10, 2)
