# Uses python3
import sys

# Time Complexity of naive: O(n), with n up to 10^18
# Optimized Algorithm: According to Pisano table, F(n) % m = F(n % Pisano period) % m,
#                      So, instead of finding Fn, we find F(n % pisano period)
#                      Pisano period is recognized by starting with 01, with being even (except for 2) and is up to m x m
# OVERALL TIME COMPLEXITY: O(m^2), with m up to 10^3
# Practically at maximum m identified, it is way less than that, as we break when the period is found,
# And the pisano period of m^3 = 1500, with stepping by 2, making the result 750 iterations


def get_fibonacci_huge_fast(n,m):

    # Calculating Pisano period
    pisano_period = 0
    # Only the Pisano period of 2 is odd, does not apply to general characteristics
    if m == 2:
        pisano_period = 3
    else:
        current = 0
        next = 1
        # Stepping by 2 as Pisano period is even, and going up to m x m until period is found
        for i in range(2, m*m, 2):
            current = (current + next) % m
            next = (current + next) % m
            if current == 0 and next == 1:
                pisano_period = i
                break

    # Applying the rule: F(n) % m = F(n % Pisano period) % m
    remainder = n % pisano_period
    current = 0
    next = 1
    # Finding F(n % Pisano period)
    for i in range(remainder):
        current, next = next, current + next
    
    return current % m

def get_fibonacci_huge_naive(n, m):

    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_fast(n, m))
    