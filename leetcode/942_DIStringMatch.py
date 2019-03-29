# https://leetcode.com/problems/di-string-match/
# "I" (increase) or "D" (decrease)
# Input: "DDI"
# Output: [3,2,0,1]

class Solution:
    def diStringMatch(self, S: str):
        lst = list(range(len(S)+1))
        res = []
        for ch in S:
            if ch == 'I':
                res.append(lst[0])
                lst = lst[1:]
            elif ch == 'D':
                res.append(lst[-1])
                lst.pop()
        res += lst
        return res


if __name__=="__main__":
    obj = Solution()
    param_1 = obj.diStringMatch("IDIDDD")
    print(param_1)
