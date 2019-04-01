class Solution:
    def isMonotonic(self, A) -> bool:
        return all(A[i]<= A[i+1] for i in range(len(A)-1)) or all(A[i]<=A[i+1] for i in range(len(A)-1))



if __name__=="__main__":
    obj = Solution()
    param_1 = obj.isMonotonic([1,2,2,3])
    print(param_1)
