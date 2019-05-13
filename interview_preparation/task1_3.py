"""
You are given an implementation of a function:
    def solution(A, K)
This function, given a non-empty array A of N integers (sorted in non-
decreasing order) and integer K, checks whether A contains number 1, 2
..., K (every number from 1 to K at least once) and no other numbers.

For example, given the following array A, and K = 3:
    A[0] = 1
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 3
The function should return True.
For the following array A, and K = 2:
    A[0] = 1
    A[1] = 1
    A[2] = 3
the function should return False.

Assume that:
    - N and K are integers within the range [1..300,000];
    - each element of array A is an integer within the range
      [0..1,000,000,000];
    - array A is sorted in non-decreasing order

In your solution, focus on correctness. Ther performance of your solution
will not be the focus of assessment.
"""

# submission, O(n) Linear Time
def solution(A, K):
    n = len(A)
    for i in range(n - 1):
        if (A[i] + 1 < A[i + 1]):
            return False
    if (A[0] != 1 or A[n - 1] != K):
        return False
    else:
        return True

# O(n2) Quadratic Time
def solution(A, K):
    n = len(A)
    if (A[0] != 1 or A[n - 1] != K):
        return False
    for i in range(1, K+1):
        if not i in A:
            return False
    return True

if __name__=="__main__":
    print(solution([1,1,3], 2))
