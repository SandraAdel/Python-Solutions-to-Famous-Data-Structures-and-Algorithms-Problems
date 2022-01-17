# Uses python3
import sys


# Naively, to get the number of inversions in array, we pass through the array elements one-by-one,
# holding each element, we iterate on all the elements after it, comparing each with it, and incrementing a counter
# that represents the number of times we have found an element whose value is the greater than the one we hold,
# counting the number of times a small value is placed after a larger value in our array
# TIME COMPLEXITY: O(n^2) --> two nested loops

# To optimize, we count the number of invserions throughout the inner steps of a sorting technique, merge sort here
# Here, we do not need to consume the memory with the auxiliary arrays needed to form the merged sorted array, 
# beacuse we only need the count of inversions, not the sorted array.
# Therefore, we simulate and keep track of the process of the merge sort algorithm with pointers on the original array, 
# "left" and "right", with the help of a temporary array "b".

# To illustrate, the merge function is simulated with get_number_of_inversions, where still the recursion base case 
# is when the length of the sub-array reaches 1, by checking the difference between the array left and right pointers
# In each recursion step, the array is divided into 2 halves, through pointers and not using auxillary arrays, 
# where both halves are sorted and merged while counting the number of inversions
# (number of smaller elements placed after ones larger than them) in the merge function simulated here by get_number_of_pairs
# and its return value is added on the number_of_inversions variable in this recursion step, adding up on all number_of_inversions values
# throughout all the recursion steps, reaching total number of inversions in the whole array at the end

# get_number_of_pairs function works with the temporary array "b" and left and right for each sub-array, as parameters
# for each sub-array, a pointer is intialized with the value of the left pointer to iterate through it
# while both the arrays are non-empty, simulated here with the pointer arrays still not reaching the value of the right pointer,
# indicating its end, the elements which both pointers of both sub-arrays are pointing are compared.
# If left sub-array element is smaller than that of the right, it is firstly copied to its same index in the temporary array  
# using both the pointers of the left sub-array and that of the temporary array, to track it, before they are both incremented.
# If right sub-array element is smaller than that of the left, that means that there is a smaller value placed after (a) larger one(s), 
# so the number_of_pairs variable is incremented with the number of elements in the left sub-array, an inversion pair for its element
# in the right sub-array with each element it is smaller than in the left-subarray. Then, it is also copied to its same index
# in the temporary array using the pointers of the right sub-array and the temporary array before incremeting them.

# two if conditions check which array is still full, its array pointer still not reaching the right pointer, 
# and its elements are copied according to their indices to the temporary array.
# Final result is that the temporary array contains the sorted merged version of the two sub-arrays,
# and its elements are respectively copied to the original array, containing the 2 sub-arrays,
# forming the basis of the next recursion step, in which other 2 sub-arrays on array "a" are merged and sorted.
# TIME COMPLEXITY: O(nxlogn) --> counting the number of inversions without adding any extra complexity to the merge sort algorithm


def get_number_of_pairs(a, b, arr1_left, arr1_right, arr2_left, arr2_right):

    # initializations:
    # number_of_pairs variable at the beginning of each call with zero
    # each sub-array pointer with the left pointer of each
    # temporary array pointer with left pointer of the first sub-array, start of working station
    number_of_pairs = 0
    arr1_ptr = arr1_left
    arr2_ptr = arr2_left
    b_ptr = arr1_left

    # while both sub-arrays are not empty, sub-array pointers not reaching their right pointers
    while arr1_ptr < arr1_right and arr2_ptr < arr2_right:

        # the element of the first sub-array pointer is compared against that of the second sub-array pointer
        if a[arr1_ptr] <= a[arr2_ptr]:
            # element is copied to its same index in temporary array
            b[b_ptr] = a[arr1_ptr]
            # incrementation of first sub-array and temporary array pointers
            arr1_ptr += 1
            b_ptr += 1

        else:
            # number_of_pairs is incremented for each pair of the right sub-array array element
            # with every element present in the left sub-array
            number_of_pairs += (arr1_right - arr1_ptr)
            # element is copied to its same index in temporary array
            b[b_ptr] = a[arr2_ptr]
            # incrementation of second sub-array and temporary array pointers
            arr2_ptr += 1
            b_ptr += 1

    # if the right sub-array is still not empty, copy its elements to the temporary array in their appropriate places
    # according to the sorted portion of array in b
    if arr2_ptr < arr2_right:
        for i in range(arr2_ptr, arr2_right):
            b[b_ptr] = a[i]
            b_ptr += 1

    # if the left sub-array is still not empty, copy its elements to the temporary array in their appropriate places
    # according to sorted portion of a in b
    elif arr1_ptr < arr1_right:
        for i in range(arr1_ptr, arr1_right):
            b[b_ptr] = a[i]
            b_ptr += 1

    # copy elements of temporary array to the part of original occupied with the left and right sub-arrays
    # beginning and end of our work station, to form the basis of the next recursion, merge and sort steps.
    for i in range(arr1_left, arr2_right):
        a[i] = b[i]

    return number_of_pairs


# Optimized get_number_of_inversions, suing merge sort algorithm
def get_number_of_inversions(a, b, left, right):
    
    # variable to place the cumulative number of inversions throughout all the recursion steps
    # and intialized with zero at the beginning of each recursion step
    number_of_inversions = 0

    # base case of recursion: array length checked through pointers
    if right - left <= 1:
        return number_of_inversions
    
    # Divison into 2 sub-arrays using left and right pointers, recusively
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)

    # counting number of inversions while merging and sorting the 2 sub-arrays, 
    # using left and right pointers for each, and a temporary array
    number_of_inversions += get_number_of_pairs(a, b, left, ave, ave, right)

    return number_of_inversions


if __name__ == '__main__':
    # DO NOT change this code
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
