# https://leetcode.com/problems/valid-parentheses/
# determine if the input string is valid.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = ''
        L = "([{"
        R = ")]}"
        A = "()"
        B = "[]"
        C = "{}"
        for ch in s:
            if ch in L:
                stack += ch
            elif ch in R:
                if stack == '':
                    return False
                elif (stack[-1] in A and ch in A) or (stack[-1] in B and ch in B) or (stack[-1] in C and ch in C):
                    stack = stack[:-1]
                else:
                    return False
        return stack == ''
            
if __name__=="__main__":
    obj = Solution()
    param_1 = obj.isValid("([)]")
    print(param_1)

# better solution also stack but using dictionary
class Solution:
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []