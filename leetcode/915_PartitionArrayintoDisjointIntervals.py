# https://leetcode.com/problems/partition-array-into-disjoint-intervals/
# smart way to find minimal of all right elements in the list

# O(n)
class Solution:
    def partitionDisjoint(self, A) -> int:
        # thus each el in B is the minimum of the right
        B = A[:]
        for i in range(len(A)-1)[::-1]:
            B[i] = min(B[i+1], A[i])
        i = 1
        left_max = A[0]
        while left_max > B[i]:
            i += 1
            left_max = max(left_max, A[i-1])
        return i


if __name__=="__main__":
    obj = Solution()
    param_1 = obj.partitionDisjoint([5,0,3,8,6])
    print(param_1)