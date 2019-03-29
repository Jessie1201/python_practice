# https://leetcode.com/problems/contains-duplicate-ii/
# HASH TABLE - using dic to update latest index for the same el

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, el in enumerate(nums):
            if el in dic and i - dic[el] <= k:
                return True
            dic[el] = i
        return False
