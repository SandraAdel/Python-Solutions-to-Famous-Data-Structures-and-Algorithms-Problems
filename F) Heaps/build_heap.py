# python3
import math


# In order to turn an array into a heap, provided that we have the parent-children connections through indices, we have to target
# all edges that may violate the heap property (top node greater than bottom node for min heap) and swap their nodes, and tracking 
# each swapped node recursively until we are sure that the heap property is satisfied in all the nodes of this sub-tree.

# As all the leaf nodes have no children, then they have no edges which may violate the heap property, so we begin checking from
# the level before the last (at depth 1) till the root at the first level, targetting greater and greater sub-trees, solving any 
# violation of the heap property (by sifting down to the leaves of this sub-tree) until we reach the result that whole tree
# is valid as heap. 
# Since each level i has a number of nodes equal to n/(2^i), then the expression floor(n/2) would approximately give the rightmost
# node in level of depth 1 to start handling. Sometimes, it gives the leftmost node in the last level, which already satisfies heap
# property. Therefore, we loop on nodes from indices floor(n/2) to 0 in a zero-indexed array.

# Eaxh violating edge is solved by calling sift_down function, which gets the left and right children of this nodes, and if any of them
# exists and has a value less than this parent, we swap their values, save their indices in the list of swaps and recursively track down
# the swapped nodes down the tree, in the direction of the smaller child (min heap), until the whole sub-tree satisfies the heap property

# In a array-saved-heap, we can find the parent-children connections on the fly through arithmatic calculations of indices.
# For a zero-indexed array, for a node i: 1) index of left child is (2xi) + 1 and 2) index of right child is (2xi) + 2

# COMPLEXITY: O(n) Actually
# We call sift_down, of complexity O(logn) n times, so the complexity should be O(nlogn). This is true, we calculate the complexity of
# sift_down based on the worst-case-scenario in the context of an individual case, not in context of a totality of n operations
# and in build_heap, we call this procedure n times.
# To illustrate, most of the called nodes are close to the leaves, so they have complexity of value much less then O(logn),
# and only the root node is the one of complexity O(logn). According to Banker's method, the cost of n sift_down operations
# can be rooted down to 2n (summing the number of nodes at each level x cost of sifting down nodes in this level)
# So, amortized cost of this procedure is O(1), called in times in build_heap --> O(n)


# Calculation of index of i's left child (zero-based indexing)
def left_child(i):
    return (2*i) + 1


# Calculation of index of i's right child (zero-based indexing)
def right_child(i):
    return (2*i) + 2


# Sifting down in the direction of the smaller child
def sift_down(i, array, swaps):

    # Assuming that the node has a value less than that of its children
    min_index = i
    size = len(array)

    # Finding left child. If it exists and has a lesser value than min_index, replace. 
    l = left_child(i)
    if l <= (size-1) and array[l] < array[min_index]:
        min_index = l

    # Finding right child. If it exists and has a lesser value than min_index, replace.
    r = right_child(i)
    if r <= (size-1) and array[r] < array[min_index]:
        min_index = r

    # If index is the same (no children or heap property is satisfied), just return swaps
    # Otherwise, update swaps list with this swap, swap the 2 nodes and recursively track
    # the newly swapped parent down the tree
    if i != min_index:
        swaps += [(i, min_index)]
        array[i], array[min_index] = array[min_index], array[i]
        swaps = sift_down(min_index, array, swaps)

    # swaps are returned as at every recursive step, so each cumulative change in it, is saved
    return swaps


def build_heap(array):
  
  # Intializing empty swaps list
    swaps = []

    # Starting from the level of depth 1 till the root level, we check on heap property
    for i in range( math.floor(len(array)/2), -1, -1 ):
        swaps = sift_down(i, array, swaps)

    return swaps


def main():
    #####   DO NOT CHANGE THE CODE IN THIS PART #########
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
