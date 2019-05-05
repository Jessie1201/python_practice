def solution(A):
    if len(A) < 2:
        return -2
    A.sort()
    minimal = A[1] - A[0]
    for i in range(len(A)-1):
        minimal = min(minimal, A[i+1] - A[i])
    if minimal > 100000000:
        return -1
    return minimal

if __name__=="__main__":
    A = [0, 100000002002]
    print(solution(A))
