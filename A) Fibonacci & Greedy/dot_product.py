#Uses python3

import sys


# Naive Algorithm: Loop in n (number of advertisments), and in each iteration,
#                  loop to find the slot with the maximum average number of clicks per day and
#                  the maximum profit per one click on ad, and add their product to the total revenue to be found
# Time Complexity of naive: O(n^2)
# Optimized Algorithm: if the arrays of average number of clicks per day of slots, and profit per each click on ad
#                      are sorted descendingly, then the first element in both arrays will always be the maximum, as
#                      we loop on n (number of advertisments)
# Complexity of greedy part of optimized algorithm: O(n)
# Sorting: To sort, we use merge sort algorithm a it has a fairly better time complexity than other sorting algorithms,
#          and a more stable one than quick sort, although the latter has better space complexity
# Merge Sort: Break down array in smaller subarrays (of one element) using recursion --> O(logn)
#             Sort the subarray elements ascendingly while working the way up and merging them again  --> O(n)
# Time Complexity of merge sort: O(nlogn)
# OVERALL TIME COMPLEXITY OF OPTIMIZED ALGORITHM: O(nlogn)


# Merging the smaller subarray elements and sorting them ascendingly,
# while working our way up after breaking down the array
def merge(first_arr, second_arr):

    sorted_array = []
    first_arr_pointer = 0
    second_arr_pointer = 0

    # While both arrays are not empty, keep comparing first element of first array with first element of second array,
    # place smaller element at the end of the merged sorted_array, and move on to the next element (incrementing the pointer)
    while first_arr_pointer < len(first_arr) and second_arr_pointer < len(second_arr):

        if first_arr[first_arr_pointer] <= second_arr[second_arr_pointer]:
            sorted_array += [first_arr[first_arr_pointer]]
            first_arr_pointer += 1
        else:
            sorted_array += [second_arr[second_arr_pointer]]
            second_arr_pointer += 1

    # Place the rest of the non-empty array at the end of the merged_sorted array, if just one of them becomes empty
    if second_arr_pointer < len(second_arr):
        for i in range(second_arr_pointer, len(second_arr)):
            sorted_array += [second_arr[i]]
    elif first_arr_pointer < len(first_arr):
        for i in range(first_arr_pointer, len(first_arr)):
            sorted_array += [first_arr[i]]

    return sorted_array


def merge_sort(array):
    
    # Base case of recurison: break down array into smaller subarrays of length one
    if len(array) == 1:
        return array

    # Keep breaking down the array using its median into two subarrays, sort and merge them 
    median = int(len(array)/2) - 1
    first_half = merge_sort(array[ : median + 1 ])
    second_half = merge_sort(array[ median + 1 : ])
    merged_sorted_array = merge(first_half, second_half)

    return merged_sorted_array

def max_dot_product(a, b):

    # Sort arrays of avg clicks of slots and profit per each click on ads
    # so as to always multiply the greatest profit per click on ad with the greatest avg number of clicks on slot
    # and get the maximum advertisement revenue
    sorted_a = merge_sort(a)
    sorted_b = merge_sort(b)
    res = 0
    for i in range(len(a)):
        res += sorted_a[i] * sorted_b[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
