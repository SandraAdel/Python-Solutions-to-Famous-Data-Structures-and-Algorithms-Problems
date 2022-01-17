#Uses python3
import sys
import numpy as np


# About the problem:
# Longest Common Subsequence is a modified version of the Edit Distance problem.
# In Edit Distance, we find the distance between 2 sequences which is the minimum number of letter substitutions (mismatches), 
# insertions and deletions done in one sequence to change it into the other among all possible allignments, so in the end we pull off a global allignment algorithm
# with the cost of matches = 0 and cost of mismatches, insertions and deletions = 1 (counting the number of changes to be done)
# and after completing the allignment table / cost matrix (referring to the DP solution: optimized), the value of the last cell is taken which represents the total cost 
# of alligning/changing the 1st sequence wholly with/to the 2nd sequnece wholly. 
# As for the Longest Common subsequence, we also globally allign the 2 sequences but do not consider the mismatch case,
# and the goal is find the maximum score of an optimal allignment where there is the most number of matches (longest common subsequnce)
# among all possible allignments, if replace the principle of cost with scores, so matches have a score of 1 and indels a score of 0.

# Naive Solution:
# This problem can be solved naively recursively by going top to bottom, where the function receives the 2 sequences as parameters,
# along with pointers pointing to the index of the last letters of each sequence, and we solve the allignment problem column by column.
# Since we do not consider mismatches, until we reach the base case of finishing either sequences (pointers turning -1), we check if we 
# have a match in the last column, if we do, then the last column is solved, we add a score of 1 to the score of the allignment between
# the first i-1 letters of 1st sequence and the second j-1 letters of the 2nd sequence, handling it column b column, which is solved 
# by the recursive call. 
# If we do not have a match, we find the maximum score of the 2 possible options of indels (gap in the second sequence: deletion)
# or (gap in the first sequence: insertion), and take it as the score of the allignment at each recursion step, so we have to go through 
# both options until the end, solving each column with the same methodology.
# COMPLEXITY: O(2^n)
# which occurs in the worst case when all the letters of both sequences mismatch. So, we have n letters, and for each letter we have 2 options,
# gap in the second sequence: deletion or gap in the first sequence: insertion, for each we find the score and take the maximum
# A complementary lag in the naive solution leading it to exponential time is the overlapping substructure of the problem, where
# the columns which are checked, the sub-problems to be solved, can be solved more than once in different parts of the tree,
# leading to many unnecessary calculations.

# Optimized Solutions using Dynamic Programming:
# Since the problem is of overlapping substructure, we avoid solving the problems which are already solved by saving the solution of each sub-problem
# in a data structure to be recalled after it is solved only once, which is the allignment matrix/table. This matrix is of size
# (length of 1st sequence +1 x length of 2nd sequence +1), as there are a zeroth column and zeroth row taken into consideration when solving the matrix.
# Each cell in the matrix is a subproblem on its own for which we find the optimal solution, so that the optimal solution of each cell leads
# to the optimal solution of the whole problem, representing the optimal substructure of the problem.
# Each cell represents the maximum score of the optimal allignment, where there is the longest common subsequence (greatest number of matches),
# between the first i letters of the 1st sequence and the first j letters of the second sequence.
# The score is calculated based on the maximum of three routes to the cell:
# 1) Diagonally ONLY if there is match, since we do not consider mismatches, and we add one to the score of the allignment in this case.
#    If this is case, it is always of greater score than the other 2 routes, since the score is incremented by 1 in this route,
#    So, we do not need to calculate the score of the other 2.
# 2) Horizontally, if there isn't a match, which means there is gap in the sequence on the rows at this cell, and we do not put a score in this case.
# 3) Vertically, also if there isn't a match which means there is gap in the sequence on the columns at this cell, and we also do not put a score in this case.
# and the highest score is placed in the cell, solution of this subproblem, as we go row by row, in each, column by column, iteratively, reaching the last cell
# starting from the first column and first row. 
# The cells of the zeroth column and row are filled with zeros as intitial values for solving the subproblems, as in the first row, we are alligning
# the 1st sequence with nothing of the 2nd sequence, and in the first column, we are alligning the 2nd sequnce with nothing of the first.
# Finally, the solution would be the value of the last cell which represents the score of the optimal allignment between
# the first i letters of 1st sequence, which is its length here, and the first j letters of the 2nd sequence, which is also its length here.
# COMPLEXITY: O(n x m)
# where n represents length of the first sequence and m the length of the second, which is the size of the part of allignment matrix we loop on,
# disregarding the zeroth column and row.


def lcs2(a, b):
    
    # Initalization of allignment matrix with zeros and starting with the first row and column,
    # So, we would have zeros in the zeroth row and column
    allignment_matrix = np.zeros((len(a)+1, len(b)+1))

    # Looping on each cell (subproblem) row-by-row first
    # and in each row column-by-column to find the optimal solution of each (maximum score)
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):

            # In case of match, its score will always be greatest than the indel options,
            # so we calculate it only and increment it with the score of one (depending on the score of the previous diagonal cell)
            # Note: the indices of both sequences lag those of the matrix by one, since we have added a zeroth column and row
            if ( a[i-1] == b[j-1] ):
                match = allignment_matrix[i-1, j-1]
                allignment_matrix[i, j] = match + 1

            # In case of mismatch, both the scores of horizontal and vertial movements are calculated (indels),
            # and the maximum of which is taken (depending on the score of the previous horizontal and vertical cells)
            else:
                insertion = allignment_matrix[i, j-1]
                deletion = allignment_matrix[i-1, j]
                allignment_matrix[i, j] = max(insertion, deletion)

    # The optimal solution of allignment of both sequences wholly is found in the last cell of the matrix
    return int(allignment_matrix[len(a), len(b)])


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
