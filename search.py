#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if index == len(array):
        return None

    elif item == array[index]:
        return index

    else:
        linear_search_recursive(array, item, index+1)




    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests below


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_recursive(array, item)
    # return binary_search_recursive(array, item)

## come back and see if you can do this without log function
def binary_search_iterative(array, item):

    low = 0
    high = len(array)

    while low <= high:
        middle = (low + high) / 2
        currentItem = array[middle]

        if currentItem == item:
            return middle
        elif item > currentItem:
            low = middle
        else:
            high = middle
    return None




    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests below


def binary_search_recursive(array, item, left=None, right=None):
    left = 0 if left is None else left
    right = len(array) if right is None else right
    mid =  (left + right) / 2
    currentItem = array[mid]

    if currentItem == item:
        return mid

    if mid >= right or mid <= left:
        return None

    elif item > currentItem:
        return binary_search_recursive(array, item, mid, right)

    else:
        return binary_search_recursive(array, item, left, mid)

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests below




if __name__ == '__main__':
    names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
    print binary_search(names, 'Winnie')
