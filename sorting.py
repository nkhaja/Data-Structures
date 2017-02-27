import math
from bst import Bst
from heap import MinHeap
''' O(n^2) always '''
def selection_sort(arr):
    if len(arr) < 2:
        return arr

    minimum = arr[0]
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                minimum = arr[j]
                arr[j] = arr[i]
                arr[i] = minimum
    return arr

''' O(n^2) , omega(n^2), if compare to front, omega(n) if compare to back '''

''' can implement with bst to get guaranteed o(n)'''
def insertion_sort(arr):
    if len(arr) < 2:
        return arr

    for i in range(1, len(arr)):
        key = arr[i]
        j = i
        # change this to look at the back instead
        while j > 0 and arr[j - 1] > key:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = key

''' best case Omega(n), worst O(n^2)'''

def bubble_sort(arr):
    if len(arr) < 2:
        return arr

    iterations = len(arr) - 1
    while iterations > 0:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
        iterations -= 1
    return arr


'''
    O(b) to allocate buckets,
    O(n) to fill buckets with n integer,
    O(n) to allocate new array that is n-long,
    O(n) to fill new output array
    ______________________________
    Result O(n+b)

    Properties:
    need small range of values (b < n),
    elements must be integers
    know(or find) min / max values

'''


def counting_sort(arr, k):
    output = []
    buckets = [0] * (k + 1)
    #what's the one liner for this?
    for i in arr:
        buckets[arr[i]] += 1

    output = []
    for index, count in enumerate(buckets):
        output.extend([index]*count)
    return output

'''

    best where values are uniformly distributed across a range
    best omega(k+n)
    worst O(k+n^2)

'''

def bucket_sort(arr, maximum, num_buckets=10):
    # create given number of buckets
    bucket_holder = [[]]*(maximum/num_buckets)
    for i in arr:
        bucket[math.ceil(i/num_buckets)] = i

    output = []
    for b in bucket_holder:
        selection_sort(b)
        output.extend(b)


def merge_sort(array):
    if len(array) <= 1:
        return array

    half = len(array)/2
    left = array[:half]
    right = array[half:]

    return merge_algorithm(merge_sort(left), merge_sort(right))


def merge_algorithm(arr1, arr2):
    output = []
    index1 = 0
    index2 = 0
    maxIterations = len(arr1) + len(arr2) - 1

    while index1 + index2 < maxIterations:
        if arr1[index1] < arr2[index2]:
            output.append(arr1[index1])
            if index1 == len(arr1) - 1:
                output.extend(arr2[index2:len(arr2)])
                break
            else:
                index1 += 1
        else:
            output.append(arr2[index2])
            if index2 == len(arr2) - 1:
                output.extend(arr1[index1:len(arr1)])
                break
            else:
                index2 += 1
    return output

def tree_sort(array):
    bst = Bst(array)
    print bst.root
    return bst.in_order(bst.root)


def heap_sort(array):
    heap = MinHeap(array)
    return list(heap.remove_min() for i in range(len(array)))



if __name__ == '__main__':
    arr = [54,25,36,89,12,34,100, 70]
    smallArr = [2,5,9,3,4,5,6,7,2,4,8,9]
    arr1 = [1,5,7]
    arr2 = [2,6,8,9]

    # print selection_sort(arr)
    # print bubble_sort(arr)
    # print counting_sort(smallArr, 9)
    # print merge_algorithm(arr1, arr2)
    # print merge_sort(arr)
    # print tree_sort(arr)

    print heap_sort(arr)
