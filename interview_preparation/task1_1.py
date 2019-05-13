"""
Write a function solution that, given two integers A and B, returns the
maximun number of repeated square root operations that can be
performed using the numbers from the interval [A...B] (both ends included)
as starting points. Square root operations can be performed as long as the result is still an integer.

For example, given A = 10, B = 20, the function should return 2. Starting
with the integer 16, two square root operations can be performed:
sqrt(16) = 4 and then sqrt(4) = 2.

Given A = 6000 and B = 7000, the function should return 3. Starting with
integer 6561, three quare root operations can be performed: sqrt(6561)
= 81, sqrt(81) = 9 and sqrt(9) = 3.

Assume that:
- A and B are integers within the range [2..10,000];
- A <= B.
"""

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