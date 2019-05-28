# Input: s = "paper", t = "title"
# Output: true
# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def getPattern(string):
            dic = {}
            for i, el in enumerate(string):
                if not el in dic:
                    dic[el] = [i]
                else:
                    dic[el].append(i)
            res = []
            for el in dic:
                if len(dic[el]) > 1:
                    res.append(dic[el])
            res.sort()
            return res
        return getPattern(s) == getPattern(t)

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.isIsomorphic("foot", "baaz")
    print(param_1)