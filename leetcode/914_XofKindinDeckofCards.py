# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
# Input: [1,2,3,4,4,3,2,1]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]

import collections
class Solution:
    def hasGroupsSizeX(self, deck) -> bool:
        count = collections.Counter(deck).values()
        div = []
        for i in range(2, min(count)+1):
            if min(count) % i == 0:
                div.append(i)
        for el in div:
            if all(num % el == 0 for num in count):
                return True
        return False

            
if __name__=="__main__":
    obj = Solution()
    param_1 = obj.hasGroupsSizeX([1,2,3,4,4,3,2,1])
    print(param_1)
