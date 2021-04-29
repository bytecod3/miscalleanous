'''
MERGESORT ALGORITHM
'''


def merge_sort(A):
    """
    :param A: List to sort
    :return: function to divide the given list
    """
    merge_sort2(A, 0, len(A)-1)


def merge_sort2(A, first, last):
    """
    :param A: List to subdivide
    :param first: starting index
    :param last: ending index
    :return: function to merge the sorted algorithms
    """
    if first < last:
        # if the list contains more than one item
        # divide the list recursively to the smallest no of items
        middle = (first + last)//2
        merge_sort2(A, first, middle)
        merge_sort2(A, middle+1, last)
        merge(A, first, middle, last)


def merge(A, first, middle, last):
    """
    :param A: list item to overwrite with the sorted list
    :param first: beginning index
    :param middle: start to subdivide here
    :param last: ending index
    :return: sorted list
    """
    L = A[first:middle]
    R = A[middle: last+1]
    L.append(99999) # append a large number to the end to help us know when the last item is reached
    R.append(99999)
    i =j = 0

    for k in range(first, last+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += i
    return A

