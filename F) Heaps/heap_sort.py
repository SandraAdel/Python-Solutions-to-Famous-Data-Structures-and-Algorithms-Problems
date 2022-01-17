#python3
import sys
import math


# Heap Sort is a fast sorting algorithm ( of complexity O(nlogn) ), which is stable ( worst and average cases are O(nlogn) 
# in comparison to Quick Sort whose average case is O(nlogn) while its worst is O(n^2) ) and is space-efficient as it sorts 
# in place using no additional memory, using the array implmentation of a heap

# Firstly, the array is turned into a heap (all edges of tree satisfying heap property) as explained in build_heap file, but
# in this case, this is a max heap, so each parent must be at least the value of its children. 
# Secondly, we loop n-1 times on the array. In each time, we swap the value of the root, which is maximum, with the value
# of the last node (rightmost leaf), putting it at the end of the array as we are sorting ascendingly. We decrease
# the size of the heap by 1, ignoring the last element which is already in its right place in the sorted array, and maintaining
# the heap property in the rest of the array, a fact that is violated if we take the last element into account.
# Lastly, we heapify (sift down) the new root so that the heap property is satisfied in the new tree.
# Here, sifting down occurs in the direction of the largest child as this is a max heap, and the heapify function takes
# size as a parameter, as it changes in each iteration and is not just the size of a

# We loop n-1 times, so we do not place the minimum value ending up at the root in the (n-1)th iteration at the end of the array
# As a result, we have an ascendingly sorted array with lesser complexiy than selection sort.
# This optimization is illustrated as in both, we iterate n times over the array elements, but the second iteration of finding
# the maximum value in selection sort is avoided by using a smart data structure such as max heap where the maximum value 
# is always at the root, the first element in the array.

# COMPLEXITY: O(nlogn)
# Since we know that the amortized analysis of build_heap is of cost O(n) from explanation in build_heap file,
# we still loop at most n times over the array, calling heapify ( O(logn) ) n times.
# And the complexity is already asymptotically optimal as this is a comparison-based sorting algorithm


# Calculation of index of i's left child (zero-based indexing)
def left_child(i):
    return (2*i) + 1


# Calculation of index of i's right child (zero-based indexing)
def right_child(i):
    return (2*i) + 2


# Sifting down in the direction of the greater child
# Size of array is passed as a parameter, as it changes as we decrement size of heap
# and is not just the size of the whole array
def heapify(i, array, size):

    # Assuming that the node has a value greater than that of its children
    max_index = i

    # Finding left child. If it exists and has a greater value than max_index, replace. 
    l = left_child(i)
    if l <= (size-1) and array[l] > array[max_index]:
        max_index = l

    # Finding right child. If it exists and has a greater value than max_index, replace.
    r = right_child(i)
    if r <= (size-1) and array[r] > array[max_index]:
        max_index = r

    # If index is the same (no children or heap property is satisfied), just return
    # Otherwise, swap the 2 nodes and recursively track the newly swapped parent down the tree
    if i != max_index:
        array[i], array[max_index] = array[max_index], array[i]
        heapify(max_index, array, size)


def build_heap(array):

    # Starting from the level of depth 1 till the root level, we check on heap property
    for i in range( math.floor(len(array)/2), -1, -1 ):
        heapify(i, array, len(array))


def heap_sort(array):
    
    # Array is turned into heap
    build_heap(array)
    size = len(array)

    # Heap property is satisfied by array still needs sorting, as the property offered a constriant
    # between the parent and children and no constraint was offered between the children and each other
    # Lopping on array n-1 times
    for i in range(1, size):

        # Swapping maximum element (at root) with last element
        array[0], array[size-1] = array[size-1], array[0]
        # Decrementing heap size, ignoring maximum value placed at the end
        size -= 1
        # Sifting down the new root until heap property is satisfied
        heapify(0, array, size)


### DO NOT CHANGE INPUT/OUTPUT FORMAT ####

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    heap_sort(a)
    for x in a:
        print(x, end=' ')

