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
