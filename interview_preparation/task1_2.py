"""
Integer V lies strictly between integers U and W if U < V < W or if U > V > W.

A non-empty array A consisting of N integers is given. A pair of indices (P,
Q), WHERE 0 <= P < Q < N, is said to have adjacent values if no value in the
array lies strictly between values A[P] and A[Q].

For example, in array A such that:
A[0] = 0
A[1] = 3
A[2] = 3
A[3] = 7
A[4] = 5
A[5] = 3
A[6] = 11
A[7] = 1
The following pairs of indices have adjacent values:
(0,7), (1,2), (1,4),
(1,5), (1,7), (2,4),
(2,5), (2,7), (3,4),
(3,6), (4,5), (5,7).

For example, indices 4 and 5 have adjacent values because ther is no
value in array A that lies strictly between A[4]=5 and A[5]=3; the only
such value could be the number 4, and it is not present in the array.

Given two indices P and Q, their distance is defined as abs(A[P]-A[Q]),
where abs(X)=X for X>=0, and abs(X)=-X for X<0. For example, the
distance between indices 4 and 5 is 2 because (A[4]-A[5])=(5-3)=2.

Write a function:
  def solution(A)
that, given a non-empty array A consisting of N integers, returns the
minimun distance between indices of this array that have adjacent
values. The function should return -1 if the minimun distance is greater
than 100,000,000. The function should return -2 if no adjacent indices
exist.

For example, given array A such that:
A[0] = 0
A[1] = 3
A[2] = 3
A[3] = 7
A[4] = 5
A[5] = 3
A[6] = 11
A[7] = 1
the function should return 0 because:
- indices 1 and 2 are adjacet, because the array does not
  contain any values that lies strictly between A[1]=3 and A[2]
  =3;
- the distance between these indices is (A[1]-A[2])=(3-3)
  =0;
- no other pair of adjacent indices that has smaller distance
  exists.

Write an efficient algorithm for the following assumtions:
- N is an integer within the range [1..40,000];
- each element of array A is an integer within the rage
  [-2,147,483,684...2,147,483,684].
"""

# O(n) Linear Time
def solution(A):
    if len(A) < 2:
        return -2
    # optimization
    if len(set(A)) != len(A):
        return 0
    # end optimization
    A.sort()
    minimal = A[1] - A[0]
    for i in range(len(A)-1):
        minimal = min(minimal, A[i+1] - A[i])
    if minimal > 100000000:
        return -1
    return minimal

# O(n2) Quadratic Time
def solution(A):
    if len(A) < 2:
        return -2
    minimal = abs(A[0] - A[1])
    for i in range(len(A)):
        new_lst = A[:i] + A[i+1:]
        minimal = min(minimal, min([abs(A[i]-el) for el in new_lst]))
    if minimal > 100000000:
        return -1
    return minimal


if __name__=="__main__":
    A = [0,3,7,5,11,2]
    print(solution(A))
