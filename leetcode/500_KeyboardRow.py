# https://leetcode.com/problems/keyboard-row/
# using letters of alphabet on only one row's of American keyboard

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        A = 'QWERTYUIOP'
        a = A.lower()
        B = 'ASDFGHJKL'
        b = B.lower()
        C = 'ZXCVBNM'
        c = C.lower()
        res = []
        for el in words:
            if all(ch in A or ch in a for ch in el) or all(ch in B or ch in b for ch in el) or all(ch in C or ch in c for ch in el):
                res.append(el)
        return res

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.isMonotonic(["Hello", "Alaska", "Dad", "Peace"])
    print(param_1)
