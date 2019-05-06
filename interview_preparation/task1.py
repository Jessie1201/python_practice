# O(n log n)
import math
def solution(A,B):
    maximum = 0
    for num in range(A,B+1):
        count = 0
        while int(math.sqrt(num)) == math.sqrt(num):
            num = math.sqrt(num)
            count += 1
        maximum = max(maximum, count)
    return maximum

# O(n log n)
def solution(A,B):
    maximum = 0
    for i in range(2, B+1):
        count = 0
        while i**2 <= B:
            i = i**2
            count += 1
        if i >= A:
            maximum = max(maximum, count)
    return maximum

# Close to my submission. # O(n log n)
def solution(A,B):
    res = []
    for i in range(2, B+1):
        count = 0
        while i**2 <= B:
            i = i**2
            count += 1
        if i >= A:
            res.append(count)
    if not res:
        return 0
    return max(res)

if __name__=="__main__":
    print(solution(6000,7000))