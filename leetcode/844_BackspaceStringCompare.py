# https://leetcode.com/problems/backspace-string-compare/
# stack solution
# '#' means a backspace character

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack = []
        for el in S:
            if el != '#':
                stack.append(el)
            elif el == '#':
                if stack:
                    stack.pop()
        S = ''.join(stack)

        stack = []
        for el in T:
            if el != '#':
                stack.append(el)
            elif el == '#':
                if stack:
                    stack.pop()
        T = ''.join(stack)

        return T == S


if __name__=="__main__":
    obj = Solution()
    param_1 = obj.backspaceCompare("ab#c", "ad#c")
    print(param_1)
