# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# find all the start indices of p's anagrams in s.
# DIFFICULT - counter out of loop; Sliding Window

import collections
class Solution:
    def findAnagrams(self, s: str, p: str):
        res = []
        # counter should be out of loop, cuz time-consuming
        a = collections.Counter(s[:len(p)-1])
        b = collections.Counter(p)
        for i in range(len(p) - 1, len(s)):
            a[s[i]] += 1
            if a == b:
                res.append(i - len(p) + 1)
            a[s[i-len(p)+1]] -= 1
            if a[s[i-len(p)+1]] == 0:
                del a[s[i-len(p)+1]]
        return res


# permutation with one line, but exeeded time
# class Solution:
#     def findAnagrams(self, s: str, p: str):
#         res = []
#         anagrams = (["".join(perm) for perm in itertools.permutations(p)])
#         for i in range(len(s)):
#             if s[i:i+len(p)] in anagrams:
#                 res.append(i)
#         return res


if __name__=="__main__":
    obj = Solution()
    param_1 = obj.findAnagrams("cbaebabacd","abc")
    print(param_1)
