# https://leetcode.com/problems/fair-candy-swap/
# exchange one candy bar each so that after the exchange, they both have 
# the same total amount of candy. 

class Solution:
    def fairCandySwap(self, A, B):
        sum_more = sum(A)
        sum_less = sum(B)
        more = A
        less = B
        if sum_more < sum_less:
            sum_more, sum_less = sum_less, sum_more
            more, less = less, more
        for el_1 in more:
            target = int(el_1 - (sum_more - sum_less) / 2)
            if target in less:
                if more == A: return [el_1, target]
                else: return [target, el_1]

if __name__=="__main__":
    obj = Solution()
    # param_1 = obj.fairCandySwap([1,1], [2,2])
    print(param_1)
