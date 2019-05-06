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
